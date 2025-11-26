import os
import uuid
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from functools import wraps

admin_bp = Blueprint('admin', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def require_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        if not current_user.is_admin:
            flash('Acces non autorise', 'error')
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function


@admin_bp.route('/')
@require_admin
def dashboard():
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


@admin_bp.route('/products')
@require_admin
def products():
    from models.database import ProductDB, CategoryDB
    products = ProductDB.query.order_by(ProductDB.order).all()
    categories = CategoryDB.query.order_by(CategoryDB.order).all()
    return render_template('admin/products.html', products=products, categories=categories)


@admin_bp.route('/products/add', methods=['GET', 'POST'])
@require_admin
def add_product():
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


@admin_bp.route('/products/<int:id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_product(id):
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


@admin_bp.route('/products/<int:id>/delete', methods=['POST'])
@require_admin
def delete_product(id):
    from app import db
    from models.database import ProductDB
    product = ProductDB.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('Produit supprime', 'success')
    return redirect(url_for('admin.products'))


@admin_bp.route('/categories')
@require_admin
def categories():
    from models.database import CategoryDB
    categories = CategoryDB.query.order_by(CategoryDB.order).all()
    return render_template('admin/categories.html', categories=categories)


@admin_bp.route('/categories/add', methods=['GET', 'POST'])
@require_admin
def add_category():
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


@admin_bp.route('/categories/<id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_category(id):
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


@admin_bp.route('/categories/<id>/delete', methods=['POST'])
@require_admin
def delete_category(id):
    from app import db
    from models.database import CategoryDB
    category = CategoryDB.query.get_or_404(id)
    if category.products:
        flash('Impossible de supprimer une categorie avec des produits', 'error')
        return redirect(url_for('admin.categories'))
    db.session.delete(category)
    db.session.commit()
    flash('Categorie supprimee', 'success')
    return redirect(url_for('admin.categories'))


@admin_bp.route('/services')
@require_admin
def services():
    from models.database import Service
    services = Service.query.order_by(Service.order).all()
    return render_template('admin/services.html', services=services)


@admin_bp.route('/services/add', methods=['GET', 'POST'])
@require_admin
def add_service():
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


@admin_bp.route('/services/<int:id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_service(id):
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


@admin_bp.route('/services/<int:id>/delete', methods=['POST'])
@require_admin
def delete_service(id):
    from app import db
    from models.database import Service
    service = Service.query.get_or_404(id)
    db.session.delete(service)
    db.session.commit()
    flash('Service supprime', 'success')
    return redirect(url_for('admin.services'))


@admin_bp.route('/partnerships')
@require_admin
def partnerships():
    from models.database import PartnershipType
    partnerships = PartnershipType.query.order_by(PartnershipType.order).all()
    return render_template('admin/partnerships.html', partnerships=partnerships)


@admin_bp.route('/partnerships/add', methods=['GET', 'POST'])
@require_admin
def add_partnership():
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


@admin_bp.route('/partnerships/<int:id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_partnership(id):
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


@admin_bp.route('/partnerships/<int:id>/delete', methods=['POST'])
@require_admin
def delete_partnership(id):
    from app import db
    from models.database import PartnershipType
    partnership = PartnershipType.query.get_or_404(id)
    db.session.delete(partnership)
    db.session.commit()
    flash('Type de partenariat supprime', 'success')
    return redirect(url_for('admin.partnerships'))


@admin_bp.route('/process')
@require_admin
def process_steps():
    from models.database import ProcessStep
    steps = ProcessStep.query.order_by(ProcessStep.order).all()
    return render_template('admin/process_steps.html', steps=steps)


@admin_bp.route('/process/add', methods=['GET', 'POST'])
@require_admin
def add_process_step():
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


@admin_bp.route('/process/<int:id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_process_step(id):
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


@admin_bp.route('/process/<int:id>/delete', methods=['POST'])
@require_admin
def delete_process_step(id):
    from app import db
    from models.database import ProcessStep
    step = ProcessStep.query.get_or_404(id)
    db.session.delete(step)
    db.session.commit()
    flash('Etape supprimee', 'success')
    return redirect(url_for('admin.process_steps'))


@admin_bp.route('/faqs')
@require_admin
def faqs():
    from models.database import FAQ
    faqs = FAQ.query.order_by(FAQ.order).all()
    return render_template('admin/faqs.html', faqs=faqs)


@admin_bp.route('/faqs/add', methods=['GET', 'POST'])
@require_admin
def add_faq():
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


@admin_bp.route('/faqs/<int:id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_faq(id):
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


@admin_bp.route('/faqs/<int:id>/delete', methods=['POST'])
@require_admin
def delete_faq(id):
    from app import db
    from models.database import FAQ
    faq = FAQ.query.get_or_404(id)
    db.session.delete(faq)
    db.session.commit()
    flash('FAQ supprimee', 'success')
    return redirect(url_for('admin.faqs'))


@admin_bp.route('/testimonials')
@require_admin
def testimonials():
    from models.database import Testimonial
    testimonials = Testimonial.query.order_by(Testimonial.order).all()
    return render_template('admin/testimonials.html', testimonials=testimonials)


@admin_bp.route('/testimonials/add', methods=['GET', 'POST'])
@require_admin
def add_testimonial():
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


@admin_bp.route('/testimonials/<int:id>/edit', methods=['GET', 'POST'])
@require_admin
def edit_testimonial(id):
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


@admin_bp.route('/testimonials/<int:id>/delete', methods=['POST'])
@require_admin
def delete_testimonial(id):
    from app import db
    from models.database import Testimonial
    testimonial = Testimonial.query.get_or_404(id)
    db.session.delete(testimonial)
    db.session.commit()
    flash('Temoignage supprime', 'success')
    return redirect(url_for('admin.testimonials'))


@admin_bp.route('/homepage')
@require_admin
def homepage():
    from app import db
    from models.database import HeroSection, HomepageStats
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
    
    return render_template('admin/homepage.html', hero=hero, stats=stats)


@admin_bp.route('/homepage/hero', methods=['POST'])
@require_admin
def update_hero():
    from app import db
    from models.database import HeroSection
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
    return redirect(url_for('admin.homepage'))


@admin_bp.route('/homepage/stats', methods=['POST'])
@require_admin
def update_stats():
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
    return redirect(url_for('admin.homepage'))


@admin_bp.route('/seo')
@require_admin
def seo():
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


@admin_bp.route('/seo/<page>', methods=['POST'])
@require_admin
def update_seo(page):
    from app import db
    from models.database import SEOSettings
    setting = SEOSettings.query.filter_by(page=page).first()
    if not setting:
        setting = SEOSettings(page=page)
        db.session.add(setting)
    
    from utils.image_processor import process_image_for_type
    
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
    flash(f'SEO de la page {page} mis a jour', 'success')
    return redirect(url_for('admin.seo'))


@admin_bp.route('/settings')
@require_admin
def settings():
    from app import db
    from models.database import ContactInfo
    contact = ContactInfo.query.first()
    if not contact:
        contact = ContactInfo()
        db.session.add(contact)
        db.session.commit()
    return render_template('admin/settings.html', contact=contact)


@admin_bp.route('/settings/contact', methods=['POST'])
@require_admin
def update_contact():
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
    contact.linkedin = request.form.get('linkedin', '')
    contact.facebook = request.form.get('facebook', '')
    contact.twitter = request.form.get('twitter', '')
    contact.youtube = request.form.get('youtube', '')
    contact.tiktok = request.form.get('tiktok', '')
    contact.pinterest = request.form.get('pinterest', '')
    
    db.session.commit()
    flash('Informations de contact mises a jour', 'success')
    return redirect(url_for('admin.settings'))


@admin_bp.route('/users')
@require_admin
def users():
    from models.database import User
    users = User.query.all()
    return render_template('admin/users.html', users=users)


@admin_bp.route('/users/<user_id>/toggle-admin', methods=['POST'])
@require_admin
def toggle_admin(user_id):
    from app import db
    from models.database import User
    user = User.query.get_or_404(user_id)
    if user.id == current_user.id:
        flash('Vous ne pouvez pas modifier vos propres droits admin', 'error')
    else:
        user.is_admin = not user.is_admin
        db.session.commit()
        flash(f'Droits admin {"accordes" if user.is_admin else "retires"} pour {user.email or user.id}', 'success')
    return redirect(url_for('admin.users'))


@admin_bp.route('/upload', methods=['POST'])
@require_admin
def upload_file():
    from utils.image_processor import process_image_for_type
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Aucun fichier selectionne'}), 400
    
    if file and allowed_file(file.filename):
        image_type = request.form.get('image_type', 'default')
        url = process_image_for_type(file, image_type)
        if url:
            return jsonify({'url': url})
        return jsonify({'error': 'Erreur lors du traitement'}), 400
    
    return jsonify({'error': 'Type de fichier non autorise'}), 400


@admin_bp.route('/upload-with-crop', methods=['POST'])
@require_admin
def upload_with_crop():
    from utils.image_processor import process_image_for_type
    
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Aucun fichier selectionne'}), 400
    
    image_type = request.form.get('image_type', 'default')
    
    crop_data = None
    if request.form.get('crop_x') is not None:
        try:
            crop_data = {
                'x': float(request.form.get('crop_x', 0)),
                'y': float(request.form.get('crop_y', 0)),
                'width': float(request.form.get('crop_width', 0)),
                'height': float(request.form.get('crop_height', 0))
            }
        except (ValueError, TypeError):
            crop_data = None
    
    url = process_image_for_type(file, image_type, crop_data)
    
    if url:
        return jsonify({'url': url, 'success': True})
    
    return jsonify({'error': 'Erreur lors du traitement de l\'image'}), 400
