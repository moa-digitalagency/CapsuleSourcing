from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'capsule-maroc-artisanat-2024'

from products import get_all_products, get_product_by_id, get_categories, get_products_by_category

@app.route('/')
def index():
    featured_products = get_all_products()[:6]
    return render_template('index.html', featured_products=featured_products)

@app.route('/catalogue')
def catalogue():
    category = request.args.get('category', 'all')
    if category == 'all':
        products = get_all_products()
    else:
        products = get_products_by_category(category)
    
    categories = get_categories()
    return render_template('catalogue.html', products=products, categories=categories, selected_category=category)

@app.route('/produit/<int:product_id>')
def product_detail(product_id):
    product = get_product_by_id(product_id)
    if product:
        related_products = get_products_by_category(product['category'])[:4]
        related_products = [p for p in related_products if p['id'] != product_id]
        return render_template('product.html', product=product, related_products=related_products)
    return "Produit non trouvé", 404

@app.route('/a-propos')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        company = request.form.get('company')
        message = request.form.get('message')
        
        return jsonify({
            'success': True,
            'message': 'Merci pour votre message ! Nous vous contacterons bientôt.'
        })
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
