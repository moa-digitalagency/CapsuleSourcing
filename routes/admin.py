import os
import uuid
import logging
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from functools import wraps

logger = logging.getLogger(__name__)

admin_bp = Blueprint('admin', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def require_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            if not current_user.is_authenticated:
                return redirect(url_for('auth.login'))
            if not current_user.is_admin:
                flash('Acces non autorise', 'error')
                return redirect(url_for('main.index'))
            return f(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in admin authentication check: {e}")
            return redirect(url_for('auth.login'))
    return decorated_function


@admin_bp.route('/')
@require_admin
def dashboard():
    try:
        from app import db
        from models.database import ProductDB, CategoryDB, Service, FAQ, User
        stats = {
            'products': ProductDB.query.count(),
            'categories': CategoryDB.query.count(),
            'services': Service.query.count(),
            'faqs': FAQ.query.count(),
            'users': User.query.count()
        }
        return render_template('admin/dashboard.html', stats=stats)
    except Exception as e:
        logger.error(f"Error in admin dashboard: {e}")
        flash('Erreur lors du chargement du tableau de bord', 'error')
        return render_template('admin/dashboard.html', stats={'products': 0, 'categories': 0, 'services': 0, 'faqs': 0, 'users': 0})


@admin_bp.route('/products')
@require_admin
def products():
    try:
        from models.database import ProductDB, CategoryDB
        products = ProductDB.query.order_by(ProductDB.order).all()
        categories = CategoryDB.query.order_by(CategoryDB.order).all()
        return render_template('admin/products.html', products=products, categories=categories)
    except Exception as e:
        logger.error(f"Error loading products: {e}")
        flash('Erreur lors du chargement des produits', 'error')
        return render_template('admin/products.html', products=[], categories=[])


@admin_bp.route('/products/add', methods=['GET', 'POST'])
@require_admin
def add_product():
    try:
        from app import db
        from models.database import ProductDB, CategoryDB
        from utils.image_processor import process_image_for_type
        categories = CategoryDB.query.order_by(CategoryDB.order).all()
        if request.method == 'POST':
            image_path = None
            if 'image' in request.files:
                file = request.files['image']
                if file and file.filename and allowed_file(file.filename):
                    image_path = process_image_for_type(file, 'product')
            
            product = ProductDB(
                name=request.form['name'],
                category_id=request.form['category_id'],
                description=request.form.get('description', ''),
                details=request.form.get('details', ''),
                dimensions=request.form.get('dimensions', ''),
                material=request.form.get('material', ''),
                image=image_path or request.form.get('image_url', ''),
                is_featured=bool(request.form.get('is_featured')),
                order=int(request.form.get('order', 0))
            )
            db.session.add(product)
            db.session.commit()
            flash('Produit ajoute avec succes', 'success')
            return redirect(url_for('admin.products'))
        return render_template('admin/product_form.html', product=None, categories=categories)
    except Exception as e:
        logger.error(f"Error adding product: {e}")
        flash('Erreur lors de l\'ajout du produit', 'error')
        return redirect(url_for('admin.products'))


@admin_bp.route('/products/<int:id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_product(id):
    try:
        from app import db
        from models.database import ProductDB, CategoryDB
        from utils.image_processor import process_image_for_type
        product = ProductDB.query.get_or_404(id)
        categories = CategoryDB.query.order_by(CategoryDB.order).all()
        if request.method == 'POST':
            if 'image' in request.files:
                file = request.files['image']
                if file and file.filename and allowed_file(file.filename):
                    new_image = process_image_for_type(file, 'product')
                    if new_image:
                        product.image = new_image
            elif request.form.get('image_url'):
                product.image = request.form['image_url']
            
            product.name = request.form['name']
            product.category_id = request.form['category_id']
            product.description = request.form.get('description', '')
            product.details = request.form.get('details', '')
            product.dimensions = request.form.get('dimensions', '')
            product.material = request.form.get('material', '')
            product.is_featured = bool(request.form.get('is_featured'))
            product.order = int(request.form.get('order', 0))
            db.session.commit()
            flash('Produit modifie avec succes', 'success')
            return redirect(url_for('admin.products'))
        return render_template('admin/product_form.html', product=product, categories=categories)
    except Exception as e:
        logger.error(f"Error editing product: {e}")
        flash('Erreur lors de la modification du produit', 'error')
        return redirect(url_for('admin.products'))


@admin_bp.route('/products/<int:id>/delete', methods=['POST'])
@require_admin
def delete_product(id):
    try:
        from app import db
        from models.database import ProductDB
        product = ProductDB.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        flash('Produit supprime', 'success')
    except Exception as e:
        logger.error(f"Error deleting product: {e}")
        flash('Erreur lors de la suppression du produit', 'error')
    return redirect(url_for('admin.products'))


@admin_bp.route('/products/<int:id>/toggle-featured', methods=['POST'])
@require_admin
def toggle_featured(id):
    try:
        from app import db
        from models.database import ProductDB
        product = ProductDB.query.get_or_404(id)
        product.is_featured = not product.is_featured
        db.session.commit()
        if product.is_featured:
            flash('Produit ajoute aux vedettes', 'success')
        else:
            flash('Produit retire des vedettes', 'success')
    except Exception as e:
        logger.error(f"Error toggling featured: {e}")
        flash('Erreur lors de la modification', 'error')
    return redirect(url_for('admin.products'))


@admin_bp.route('/categories')
@require_admin
def categories():
    try:
        from models.database import CategoryDB
        categories = CategoryDB.query.order_by(CategoryDB.order).all()
        return render_template('admin/categories.html', categories=categories)
    except Exception as e:
        logger.error(f"Error loading categories: {e}")
        flash('Erreur lors du chargement des categories', 'error')
        return render_template('admin/categories.html', categories=[])


@admin_bp.route('/categories/add', methods=['GET', 'POST'])
@require_admin
def add_category():
    try:
        from app import db
        from models.database import CategoryDB
        if request.method == 'POST':
            category = CategoryDB(
                id=request.form['id'],
                name=request.form['name'],
                icon=request.form.get('icon', ''),
                order=int(request.form.get('order', 0))
            )
            db.session.add(category)
            db.session.commit()
            flash('Categorie ajoutee avec succes', 'success')
            return redirect(url_for('admin.categories'))
        return render_template('admin/category_form.html', category=None)
    except Exception as e:
        logger.error(f"Error adding category: {e}")
        flash('Erreur lors de l\'ajout de la categorie', 'error')
        return redirect(url_for('admin.categories'))


@admin_bp.route('/categories/<id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_category(id):
    try:
        from app import db
        from models.database import CategoryDB
        category = CategoryDB.query.get_or_404(id)
        if request.method == 'POST':
            category.name = request.form['name']
            category.icon = request.form.get('icon', '')
            category.order = int(request.form.get('order', 0))
            db.session.commit()
            flash('Categorie modifiee avec succes', 'success')
            return redirect(url_for('admin.categories'))
        return render_template('admin/category_form.html', category=category)
    except Exception as e:
        logger.error(f"Error editing category: {e}")
        flash('Erreur lors de la modification de la categorie', 'error')
        return redirect(url_for('admin.categories'))


@admin_bp.route('/categories/<id>/delete', methods=['POST'])
@require_admin
def delete_category(id):
    try:
        from app import db
        from models.database import CategoryDB
        category = CategoryDB.query.get_or_404(id)
        if category.products:
            flash('Impossible de supprimer une categorie avec des produits', 'error')
            return redirect(url_for('admin.categories'))
        db.session.delete(category)
        db.session.commit()
        flash('Categorie supprimee', 'success')
    except Exception as e:
        logger.error(f"Error deleting category: {e}")
        flash('Erreur lors de la suppression de la categorie', 'error')
    return redirect(url_for('admin.categories'))


@admin_bp.route('/services')
@require_admin
def services():
    try:
        from models.database import Service
        services = Service.query.order_by(Service.order).all()
        return render_template('admin/services.html', services=services)
    except Exception as e:
        logger.error(f"Error loading services: {e}")
        flash('Erreur lors du chargement des services', 'error')
        return render_template('admin/services.html', services=[])


@admin_bp.route('/services/add', methods=['GET', 'POST'])
@require_admin
def add_service():
    try:
        from app import db
        from models.database import Service
        if request.method == 'POST':
            service = Service(
                title=request.form['title'],
                description=request.form.get('description', ''),
                icon=request.form.get('icon', ''),
                order=int(request.form.get('order', 0))
            )
            db.session.add(service)
            db.session.commit()
            flash('Service ajoute avec succes', 'success')
            return redirect(url_for('admin.services'))
        return render_template('admin/service_form.html', service=None)
    except Exception as e:
        logger.error(f"Error adding service: {e}")
        flash('Erreur lors de l\'ajout du service', 'error')
        return redirect(url_for('admin.services'))


@admin_bp.route('/services/<int:id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_service(id):
    try:
        from app import db
        from models.database import Service
        service = Service.query.get_or_404(id)
        if request.method == 'POST':
            service.title = request.form['title']
            service.description = request.form.get('description', '')
            service.icon = request.form.get('icon', '')
            service.order = int(request.form.get('order', 0))
            db.session.commit()
            flash('Service modifie avec succes', 'success')
            return redirect(url_for('admin.services'))
        return render_template('admin/service_form.html', service=service)
    except Exception as e:
        logger.error(f"Error editing service: {e}")
        flash('Erreur lors de la modification du service', 'error')
        return redirect(url_for('admin.services'))


@admin_bp.route('/services/<int:id>/delete', methods=['POST'])
@require_admin
def delete_service(id):
    try:
        from app import db
        from models.database import Service
        service = Service.query.get_or_404(id)
        db.session.delete(service)
        db.session.commit()
        flash('Service supprime', 'success')
    except Exception as e:
        logger.error(f"Error deleting service: {e}")
        flash('Erreur lors de la suppression du service', 'error')
    return redirect(url_for('admin.services'))


@admin_bp.route('/partnerships')
@require_admin
def partnerships():
    try:
        from models.database import PartnershipType
        partnerships = PartnershipType.query.order_by(PartnershipType.order).all()
        return render_template('admin/partnerships.html', partnerships=partnerships)
    except Exception as e:
        logger.error(f"Error loading partnerships: {e}")
        flash('Erreur lors du chargement des partenariats', 'error')
        return render_template('admin/partnerships.html', partnerships=[])


@admin_bp.route('/partnerships/add', methods=['GET', 'POST'])
@require_admin
def add_partnership():
    try:
        from app import db
        from models.database import PartnershipType
        if request.method == 'POST':
            partnership = PartnershipType(
                title=request.form['title'],
                description=request.form.get('description', ''),
                benefits=request.form.get('benefits', ''),
                order=int(request.form.get('order', 0))
            )
            db.session.add(partnership)
            db.session.commit()
            flash('Type de partenariat ajoute avec succes', 'success')
            return redirect(url_for('admin.partnerships'))
        return render_template('admin/partnership_form.html', partnership=None)
    except Exception as e:
        logger.error(f"Error adding partnership: {e}")
        flash('Erreur lors de l\'ajout du partenariat', 'error')
        return redirect(url_for('admin.partnerships'))


@admin_bp.route('/partnerships/<int:id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_partnership(id):
    try:
        from app import db
        from models.database import PartnershipType
        partnership = PartnershipType.query.get_or_404(id)
        if request.method == 'POST':
            partnership.title = request.form['title']
            partnership.description = request.form.get('description', '')
            partnership.benefits = request.form.get('benefits', '')
            partnership.order = int(request.form.get('order', 0))
            db.session.commit()
            flash('Type de partenariat modifie avec succes', 'success')
            return redirect(url_for('admin.partnerships'))
        return render_template('admin/partnership_form.html', partnership=partnership)
    except Exception as e:
        logger.error(f"Error editing partnership: {e}")
        flash('Erreur lors de la modification du partenariat', 'error')
        return redirect(url_for('admin.partnerships'))


@admin_bp.route('/partnerships/<int:id>/delete', methods=['POST'])
@require_admin
def delete_partnership(id):
    try:
        from app import db
        from models.database import PartnershipType
        partnership = PartnershipType.query.get_or_404(id)
        db.session.delete(partnership)
        db.session.commit()
        flash('Type de partenariat supprime', 'success')
    except Exception as e:
        logger.error(f"Error deleting partnership: {e}")
        flash('Erreur lors de la suppression du partenariat', 'error')
    return redirect(url_for('admin.partnerships'))


@admin_bp.route('/process')
@require_admin
def process_steps():
    try:
        from models.database import ProcessStep
        steps = ProcessStep.query.order_by(ProcessStep.order).all()
        return render_template('admin/process_steps.html', steps=steps)
    except Exception as e:
        logger.error(f"Error loading process steps: {e}")
        flash('Erreur lors du chargement des etapes', 'error')
        return render_template('admin/process_steps.html', steps=[])


@admin_bp.route('/process/add', methods=['GET', 'POST'])
@require_admin
def add_process_step():
    try:
        from app import db
        from models.database import ProcessStep
        if request.method == 'POST':
            step = ProcessStep(
                number=request.form['number'],
                title=request.form['title'],
                description=request.form.get('description', ''),
                order=int(request.form.get('order', 0))
            )
            db.session.add(step)
            db.session.commit()
            flash('Etape ajoutee avec succes', 'success')
            return redirect(url_for('admin.process_steps'))
        return render_template('admin/process_step_form.html', step=None)
    except Exception as e:
        logger.error(f"Error adding process step: {e}")
        flash('Erreur lors de l\'ajout de l\'etape', 'error')
        return redirect(url_for('admin.process_steps'))


@admin_bp.route('/process/<int:id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_process_step(id):
    try:
        from app import db
        from models.database import ProcessStep
        step = ProcessStep.query.get_or_404(id)
        if request.method == 'POST':
            step.number = request.form['number']
            step.title = request.form['title']
            step.description = request.form.get('description', '')
            step.order = int(request.form.get('order', 0))
            db.session.commit()
            flash('Etape modifiee avec succes', 'success')
            return redirect(url_for('admin.process_steps'))
        return render_template('admin/process_step_form.html', step=step)
    except Exception as e:
        logger.error(f"Error editing process step: {e}")
        flash('Erreur lors de la modification de l\'etape', 'error')
        return redirect(url_for('admin.process_steps'))


@admin_bp.route('/process/<int:id>/delete', methods=['POST'])
@require_admin
def delete_process_step(id):
    try:
        from app import db
        from models.database import ProcessStep
        step = ProcessStep.query.get_or_404(id)
        db.session.delete(step)
        db.session.commit()
        flash('Etape supprimee', 'success')
    except Exception as e:
        logger.error(f"Error deleting process step: {e}")
        flash('Erreur lors de la suppression de l\'etape', 'error')
    return redirect(url_for('admin.process_steps'))


@admin_bp.route('/faqs')
@require_admin
def faqs():
    try:
        from models.database import FAQ
        faqs = FAQ.query.order_by(FAQ.order).all()
        return render_template('admin/faqs.html', faqs=faqs)
    except Exception as e:
        logger.error(f"Error loading FAQs: {e}")
        flash('Erreur lors du chargement des FAQs', 'error')
        return render_template('admin/faqs.html', faqs=[])


@admin_bp.route('/faqs/add', methods=['GET', 'POST'])
@require_admin
def add_faq():
    try:
        from app import db
        from models.database import FAQ
        if request.method == 'POST':
            faq = FAQ(
                question=request.form['question'],
                answer=request.form.get('answer', ''),
                order=int(request.form.get('order', 0))
            )
            db.session.add(faq)
            db.session.commit()
            flash('FAQ ajoutee avec succes', 'success')
            return redirect(url_for('admin.faqs'))
        return render_template('admin/faq_form.html', faq=None)
    except Exception as e:
        logger.error(f"Error adding FAQ: {e}")
        flash('Erreur lors de l\'ajout de la FAQ', 'error')
        return redirect(url_for('admin.faqs'))


@admin_bp.route('/faqs/<int:id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_faq(id):
    try:
        from app import db
        from models.database import FAQ
        faq = FAQ.query.get_or_404(id)
        if request.method == 'POST':
            faq.question = request.form['question']
            faq.answer = request.form.get('answer', '')
            faq.order = int(request.form.get('order', 0))
            db.session.commit()
            flash('FAQ modifiee avec succes', 'success')
            return redirect(url_for('admin.faqs'))
        return render_template('admin/faq_form.html', faq=faq)
    except Exception as e:
        logger.error(f"Error editing FAQ: {e}")
        flash('Erreur lors de la modification de la FAQ', 'error')
        return redirect(url_for('admin.faqs'))


@admin_bp.route('/faqs/<int:id>/delete', methods=['POST'])
@require_admin
def delete_faq(id):
    try:
        from app import db
        from models.database import FAQ
        faq = FAQ.query.get_or_404(id)
        db.session.delete(faq)
        db.session.commit()
        flash('FAQ supprimee', 'success')
    except Exception as e:
        logger.error(f"Error deleting FAQ: {e}")
        flash('Erreur lors de la suppression de la FAQ', 'error')
    return redirect(url_for('admin.faqs'))


@admin_bp.route('/testimonials')
@require_admin
def testimonials():
    try:
        from models.database import Testimonial
        testimonials = Testimonial.query.order_by(Testimonial.order).all()
        return render_template('admin/testimonials.html', testimonials=testimonials)
    except Exception as e:
        logger.error(f"Error loading testimonials: {e}")
        flash('Erreur lors du chargement des temoignages', 'error')
        return render_template('admin/testimonials.html', testimonials=[])


@admin_bp.route('/testimonials/add', methods=['GET', 'POST'])
@require_admin
def add_testimonial():
    try:
        from app import db
        from models.database import Testimonial
        from utils.image_processor import process_image_for_type
        if request.method == 'POST':
            image_path = None
            if 'author_image' in request.files:
                file = request.files['author_image']
                if file and file.filename and allowed_file(file.filename):
                    image_path = process_image_for_type(file, 'testimonial')
            
            testimonial = Testimonial(
                text=request.form['text'],
                author_name=request.form['author_name'],
                author_title=request.form.get('author_title', ''),
                author_image=image_path or request.form.get('author_image_url', ''),
                order=int(request.form.get('order', 0))
            )
            db.session.add(testimonial)
            db.session.commit()
            flash('Temoignage ajoute avec succes', 'success')
            return redirect(url_for('admin.testimonials'))
        return render_template('admin/testimonial_form.html', testimonial=None)
    except Exception as e:
        logger.error(f"Error adding testimonial: {e}")
        flash('Erreur lors de l\'ajout du temoignage', 'error')
        return redirect(url_for('admin.testimonials'))


@admin_bp.route('/testimonials/<int:id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_testimonial(id):
    try:
        from app import db
        from models.database import Testimonial
        from utils.image_processor import process_image_for_type
        testimonial = Testimonial.query.get_or_404(id)
        if request.method == 'POST':
            if 'author_image' in request.files:
                file = request.files['author_image']
                if file and file.filename and allowed_file(file.filename):
                    new_image = process_image_for_type(file, 'testimonial')
                    if new_image:
                        testimonial.author_image = new_image
            elif request.form.get('author_image_url'):
                testimonial.author_image = request.form['author_image_url']
            
            testimonial.text = request.form['text']
            testimonial.author_name = request.form['author_name']
            testimonial.author_title = request.form.get('author_title', '')
            testimonial.order = int(request.form.get('order', 0))
            db.session.commit()
            flash('Temoignage modifie avec succes', 'success')
            return redirect(url_for('admin.testimonials'))
        return render_template('admin/testimonial_form.html', testimonial=testimonial)
    except Exception as e:
        logger.error(f"Error editing testimonial: {e}")
        flash('Erreur lors de la modification du temoignage', 'error')
        return redirect(url_for('admin.testimonials'))


@admin_bp.route('/testimonials/<int:id>/delete', methods=['POST'])
@require_admin
def delete_testimonial(id):
    try:
        from app import db
        from models.database import Testimonial
        testimonial = Testimonial.query.get_or_404(id)
        db.session.delete(testimonial)
        db.session.commit()
        flash('Temoignage supprime', 'success')
    except Exception as e:
        logger.error(f"Error deleting testimonial: {e}")
        flash('Erreur lors de la suppression du temoignage', 'error')
    return redirect(url_for('admin.testimonials'))


@admin_bp.route('/homepage')
@require_admin
def homepage():
    try:
        from app import db
        from models.database import HeroSection, HomepageStats, ProductDB
        hero = HeroSection.query.first()
        if not hero:
            hero = HeroSection()
            db.session.add(hero)
            db.session.commit()
        
        stats = HomepageStats.query.first()
        if not stats:
            stats = HomepageStats()
            db.session.add(stats)
            db.session.commit()
        
        products = ProductDB.query.order_by(ProductDB.order).all()
        
        return render_template('admin/homepage.html', hero=hero, stats=stats, products=products)
    except Exception as e:
        logger.error(f"Error loading homepage settings: {e}")
        flash('Erreur lors du chargement des parametres', 'error')
        return render_template('admin/homepage.html', hero=None, stats=None, products=[])


@admin_bp.route('/homepage/hero', methods=['POST'])
@require_admin
def update_hero():
    try:
        from app import db
        from models.database import HeroSection, ProductDB
        from utils.image_processor import process_image_for_type
        hero = HeroSection.query.first()
        if not hero:
            hero = HeroSection()
            db.session.add(hero)
        
        hero.title = request.form.get('title', hero.title)
        hero.subtitle = request.form.get('subtitle', hero.subtitle)
        hero.button_text = request.form.get('button_text', hero.button_text)
        hero.card1_title = request.form.get('card1_title', hero.card1_title)
        hero.card1_subtitle = request.form.get('card1_subtitle', hero.card1_subtitle)
        hero.card1_link = request.form.get('card1_link', hero.card1_link)
        hero.card2_title = request.form.get('card2_title', hero.card2_title)
        hero.card2_subtitle = request.form.get('card2_subtitle', hero.card2_subtitle)
        hero.card2_link = request.form.get('card2_link', hero.card2_link)
        
        product_fields = {
            'main_product_id': 'main_image',
            'card1_product_id': 'card1_image',
            'card2_product_id': 'card2_image'
        }
        for product_field, image_field in product_fields.items():
            product_id = request.form.get(product_field)
            if product_id:
                product = ProductDB.query.get(int(product_id))
                if product and product.image:
                    setattr(hero, image_field, product.image)
        
        image_types = {'main_image': 'hero_main', 'card1_image': 'hero_card', 'card2_image': 'hero_card'}
        for field, img_type in image_types.items():
            if field in request.files:
                file = request.files[field]
                if file and file.filename and allowed_file(file.filename):
                    new_image = process_image_for_type(file, img_type)
                    if new_image:
                        setattr(hero, field, new_image)
        
        db.session.commit()
        flash('Section hero mise a jour', 'success')
    except Exception as e:
        logger.error(f"Error updating hero: {e}")
        flash('Erreur lors de la mise a jour du hero', 'error')
    return redirect(url_for('admin.homepage'))


@admin_bp.route('/homepage/stats', methods=['POST'])
@require_admin
def update_stats():
    try:
        from app import db
        from models.database import HomepageStats
        stats = HomepageStats.query.first()
        if not stats:
            stats = HomepageStats()
            db.session.add(stats)
        
        stats.artisans = int(request.form.get('artisans', 50))
        stats.products = int(request.form.get('products', 200))
        stats.partners = int(request.form.get('partners', 35))
        stats.countries = int(request.form.get('countries', 12))
        
        db.session.commit()
        flash('Statistiques mises a jour', 'success')
    except Exception as e:
        logger.error(f"Error updating stats: {e}")
        flash('Erreur lors de la mise a jour des statistiques', 'error')
    return redirect(url_for('admin.homepage'))


@admin_bp.route('/seo')
@require_admin
def seo():
    try:
        from app import db
        from models.database import SEOSettings
        pages = ['index', 'catalogue', 'about', 'contact', 'services', 'partenariats', 'processus', 'faq']
        seo_settings = {}
        for page in pages:
            setting = SEOSettings.query.filter_by(page=page).first()
            if not setting:
                setting = SEOSettings(page=page)
                db.session.add(setting)
            seo_settings[page] = setting
        db.session.commit()
        return render_template('admin/seo.html', seo_settings=seo_settings, pages=pages)
    except Exception as e:
        logger.error(f"Error loading SEO settings: {e}")
        flash('Erreur lors du chargement des parametres SEO', 'error')
        return render_template('admin/seo.html', seo_settings={}, pages=[])


@admin_bp.route('/seo/<page>', methods=['POST'])
@require_admin
def update_seo(page):
    try:
        from app import db
        from models.database import SEOSettings
        from utils.image_processor import process_image_for_type
        
        setting = SEOSettings.query.filter_by(page=page).first()
        if not setting:
            setting = SEOSettings(page=page)
            db.session.add(setting)
        
        setting.meta_title = request.form.get('meta_title', '')
        setting.meta_description = request.form.get('meta_description', '')
        setting.meta_keywords = request.form.get('meta_keywords', '')
        setting.og_title = request.form.get('og_title', '')
        setting.og_description = request.form.get('og_description', '')
        
        if 'og_image' in request.files:
            file = request.files['og_image']
            if file and file.filename and allowed_file(file.filename):
                new_image = process_image_for_type(file, 'og_image')
                if new_image:
                    setting.og_image = new_image
        
        db.session.commit()
        flash(f'SEO pour {page} mis a jour', 'success')
    except Exception as e:
        logger.error(f"Error updating SEO for {page}: {e}")
        flash('Erreur lors de la mise a jour du SEO', 'error')
    return redirect(url_for('admin.seo'))


@admin_bp.route('/contact-info')
@require_admin
def contact_info():
    try:
        from app import db
        from models.database import ContactInfo
        contact = ContactInfo.query.first()
        if not contact:
            contact = ContactInfo()
            db.session.add(contact)
            db.session.commit()
        return render_template('admin/contact_info.html', contact=contact)
    except Exception as e:
        logger.error(f"Error loading contact info: {e}")
        flash('Erreur lors du chargement des informations de contact', 'error')
        return render_template('admin/contact_info.html', contact=None)


@admin_bp.route('/contact-info', methods=['POST'])
@require_admin
def update_contact_info():
    try:
        from app import db
        from models.database import ContactInfo
        contact = ContactInfo.query.first()
        if not contact:
            contact = ContactInfo()
            db.session.add(contact)
        
        contact.email = request.form.get('email', '')
        contact.phone = request.form.get('phone', '')
        contact.whatsapp = request.form.get('whatsapp', '')
        contact.address = request.form.get('address', '')
        contact.instagram = request.form.get('instagram', '')
        contact.facebook = request.form.get('facebook', '')
        contact.tiktok = request.form.get('tiktok', '')
        
        db.session.commit()
        flash('Informations de contact mises a jour', 'success')
    except Exception as e:
        logger.error(f"Error updating contact info: {e}")
        flash('Erreur lors de la mise a jour des informations de contact', 'error')
    return redirect(url_for('admin.contact_info'))


@admin_bp.route('/highlights')
@require_admin
def featured_highlights():
    try:
        from models.database import FeaturedHighlight
        highlights = FeaturedHighlight.query.order_by(FeaturedHighlight.slot).all()
        return render_template('admin/featured_highlights.html', highlights=highlights)
    except Exception as e:
        logger.error(f"Error loading highlights: {e}")
        flash('Erreur lors du chargement des mises en avant', 'error')
        return render_template('admin/featured_highlights.html', highlights=[])


@admin_bp.route('/highlights/<int:id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_featured_highlight(id):
    try:
        from app import db
        from models.database import FeaturedHighlight
        from utils.image_processor import process_image_for_type
        highlight = FeaturedHighlight.query.get_or_404(id)
        if request.method == 'POST':
            if 'image' in request.files:
                file = request.files['image']
                if file and file.filename and allowed_file(file.filename):
                    new_image = process_image_for_type(file, 'featured_highlight')
                    if new_image:
                        highlight.image = new_image
            elif request.form.get('image_url'):
                highlight.image = request.form['image_url']
            
            highlight.title = request.form.get('title', '')
            highlight.subtitle = request.form.get('subtitle', '')
            highlight.badge = request.form.get('badge', '')
            highlight.link = request.form.get('link', '')
            highlight.link_text = request.form.get('link_text', '')
            highlight.is_active = bool(request.form.get('is_active'))
            
            db.session.commit()
            flash('Mise en avant modifiee avec succes', 'success')
            return redirect(url_for('admin.featured_highlights'))
        return render_template('admin/featured_highlight_form.html', highlight=highlight)
    except Exception as e:
        logger.error(f"Error editing highlight: {e}")
        flash('Erreur lors de la modification de la mise en avant', 'error')
        return redirect(url_for('admin.featured_highlights'))


@admin_bp.route('/page-content')
@require_admin
def page_content():
    try:
        from models.database import PageContent
        pages = PageContent.query.order_by(PageContent.page).all()
        return render_template('admin/page_content.html', pages=pages)
    except Exception as e:
        logger.error(f"Error loading page content: {e}")
        flash('Erreur lors du chargement du contenu des pages', 'error')
        return render_template('admin/page_content.html', pages=[])


@admin_bp.route('/page-content/<int:id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_page_content(id):
    try:
        from app import db
        from models.database import PageContent
        content = PageContent.query.get_or_404(id)
        if request.method == 'POST':
            import json
            try:
                content.content = json.loads(request.form.get('content', '{}'))
            except json.JSONDecodeError:
                flash('Contenu JSON invalide', 'error')
                return render_template('admin/page_content_form.html', content=content)
            
            db.session.commit()
            flash('Contenu de la page mis a jour', 'success')
            return redirect(url_for('admin.page_content'))
        return render_template('admin/page_content_form.html', content=content)
    except Exception as e:
        logger.error(f"Error editing page content: {e}")
        flash('Erreur lors de la modification du contenu de la page', 'error')
        return redirect(url_for('admin.page_content'))
