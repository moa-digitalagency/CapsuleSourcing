from flask import render_template, request, jsonify
from routes import main_bp
from services.product_service import ProductService
from services.content_service import get_page_content, get_section_content

product_service = ProductService()


@main_bp.route('/')
def index():
    from models.database import (
        HeroSection, HomepageStats, Testimonial, ProcessStep, ContactInfo
    )
    
    featured_products = product_service.get_featured_products(limit=8)
    
    hero = HeroSection.query.first()
    stats = HomepageStats.query.first()
    testimonials = Testimonial.query.order_by(Testimonial.order).all()
    process_steps = ProcessStep.query.order_by(ProcessStep.order).limit(4).all()
    contact_info = ContactInfo.query.first()
    
    content = get_page_content('index')
    
    return render_template('index.html', 
        featured_products=featured_products, 
        hero=hero,
        stats=stats,
        testimonials=testimonials,
        process_steps=process_steps,
        contact_info=contact_info,
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
