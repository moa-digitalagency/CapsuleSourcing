from flask import render_template, request, jsonify
from routes import main_bp
from services.product_service import ProductService

product_service = ProductService()


@main_bp.route('/')
def index():
    featured_products = product_service.get_featured_products(limit=8)
    stats = {
        'artisans': 50,
        'products': 200,
        'partners': 35,
        'countries': 12
    }
    return render_template('index.html', featured_products=featured_products, stats=stats)


@main_bp.route('/a-propos')
def about():
    return render_template('about.html')


@main_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        company = request.form.get('company')
        message = request.form.get('message')
        
        return jsonify({
            'success': True,
            'message': 'Merci pour votre message ! Nous vous contacterons bientot.'
        })
    
    return render_template('contact.html')
