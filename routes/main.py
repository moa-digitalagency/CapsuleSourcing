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
    
    all_highlights = FeaturedHighlight.query.order_by(FeaturedHighlight.slot).all()
    
    if len(all_highlights) < 5:
        default_data = [
            {'slot': 1, 'title': 'Poterie Traditionnelle', 'subtitle': 'Pieces uniques faconnees selon les techniques ancestrales de Fes et Safi. Chaque creation porte l\'empreinte du maitre artisan qui l\'a realisee.', 'badge': 'CERAMIQUE ET POTERIE', 'link': '/catalogue?category=ceramique', 'link_text': 'Decouvrir la Collection', 'image': '/static/images/moroccan_pottery_cer_26051764.jpg', 'is_active': True},
            {'slot': 2, 'title': 'Ex-voto en Laiton', 'subtitle': 'Laiton martele', 'badge': '', 'link': '/catalogue?category=metal', 'link_text': 'Voir le produit', 'image': '/static/images/moroccan_brass_craft_5197c08b.jpg', 'is_active': True},
            {'slot': 3, 'title': 'Miroirs Artisanaux', 'subtitle': 'Bois sculpte a la main', 'badge': '', 'link': '/catalogue?category=mobilier', 'link_text': 'Voir le produit', 'image': '/static/images/moroccan_woodwork_fu_74825e67.jpg', 'is_active': True},
            {'slot': 4, 'title': 'Mini Cadre Identite', 'subtitle': 'Laiton', 'badge': '', 'link': '/catalogue?category=metal', 'link_text': 'Voir le produit', 'image': '/static/images/moroccan_brass_craft_91c1b440.jpg', 'is_active': True},
            {'slot': 5, 'title': 'Solitore Mural en Laiton', 'subtitle': 'Laiton poli', 'badge': '', 'link': '/catalogue?category=metal', 'link_text': 'Voir le produit', 'image': '/static/images/moroccan_brass_metal_6cc61071.jpg', 'is_active': True},
        ]
        existing_slots = [h.slot for h in all_highlights]
        for data in default_data:
            if data['slot'] not in existing_slots:
                highlight = FeaturedHighlight(**data)
                db.session.add(highlight)
        db.session.commit()
    
    highlights = FeaturedHighlight.query.filter_by(is_active=True).order_by(FeaturedHighlight.slot).limit(5).all()
    
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
