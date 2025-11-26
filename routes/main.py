from flask import render_template, request, jsonify
from routes import main_bp
from services.product_service import ProductService
from services.content_service import get_page_content, get_section_content

product_service = ProductService()


@main_bp.route('/')
def index():
    from models.database import (
        HeroSection, HomepageStats, Testimonial, ProcessStep, ContactInfo, FeaturedHighlight
    )
    from app import db
    
    featured_products = product_service.get_featured_products(limit=8)
    
    hero = HeroSection.query.first()
    stats = HomepageStats.query.first()
    testimonials = Testimonial.query.order_by(Testimonial.order).all()
    process_steps = ProcessStep.query.order_by(ProcessStep.order).limit(4).all()
    contact_info = ContactInfo.query.first()
    
    highlights = FeaturedHighlight.query.filter_by(is_active=True).order_by(FeaturedHighlight.slot).all()
    
    if len(highlights) < 4:
        default_data = [
            {'slot': 1, 'title': 'Ceramique & Poterie', 'subtitle': 'Pieces uniques de Fes et Safi', 'badge': 'Collection', 'link': '/catalogue?category=ceramique', 'image': '/static/images/moroccan_pottery_cer_26051764.jpg'},
            {'slot': 2, 'title': 'Maroquinerie', 'subtitle': 'Cuir tanne traditionnellement', 'badge': 'Artisanat', 'link': '/catalogue?category=cuir', 'image': '/static/images/moroccan_leather_cra_5f8fd31d.jpg'},
            {'slot': 3, 'title': 'Ebenisterie', 'subtitle': 'Bois sculpte et peint a la main', 'badge': 'Artisanat', 'link': '/catalogue?category=mobilier', 'image': '/static/images/moroccan_woodwork_fu_74825e67.jpg'},
            {'slot': 4, 'title': 'Dinanderie', 'subtitle': 'Travail du cuivre et laiton', 'badge': 'Artisanat', 'link': '/catalogue?category=metal', 'image': '/static/images/moroccan_brass_metal_4be139c4.jpg'},
        ]
        existing_slots = [h.slot for h in highlights]
        for data in default_data:
            if data['slot'] not in existing_slots:
                highlight = FeaturedHighlight(**data)
                db.session.add(highlight)
        db.session.commit()
        highlights = FeaturedHighlight.query.filter_by(is_active=True).order_by(FeaturedHighlight.slot).limit(4).all()
    
    content = get_page_content('index')
    
    return render_template('index.html', 
        featured_products=featured_products, 
        hero=hero,
        stats=stats,
        testimonials=testimonials,
        process_steps=process_steps,
        contact_info=contact_info,
        highlights=highlights,
        content=content
    )


@main_bp.route('/a-propos')
def about():
    from models.database import ContactInfo
    
    contact_info = ContactInfo.query.first()
    content = get_page_content('about')
    
    return render_template('about.html', contact_info=contact_info, content=content)


@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    from models.database import ContactInfo
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        company = request.form.get('company')
        message = request.form.get('message')
        
        return jsonify({
            'success': True,
            'message': 'Merci pour votre message ! Nous vous contacterons bientot.'
        })
    
    contact_info = ContactInfo.query.first()
    content = get_page_content('contact')
    
    return render_template('contact.html', contact_info=contact_info, content=content)
