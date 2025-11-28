from flask import render_template, request
from routes import catalogue_bp
from services.product_service import ProductService
import logging

logger = logging.getLogger(__name__)
product_service = ProductService()


@catalogue_bp.route('/catalogue')
def catalogue():
    try:
        category = request.args.get('category', 'all')
        products = product_service.get_products_by_category(category)
        categories = product_service.get_categories()
        return render_template(
            'catalogue.html', 
            products=products, 
            categories=categories, 
            selected_category=category
        )
    except Exception as e:
        logger.error(f"Error in catalogue route: {e}")
        return render_template('errors/500.html'), 500


@catalogue_bp.route('/produit/<int:product_id>')
def product_detail(product_id):
    try:
        product = product_service.get_product_by_id(product_id)
        if product:
            related_products = product_service.get_related_products(product, limit=4)
            return render_template('product.html', product=product, related_products=related_products)
        return render_template('errors/404.html'), 404
    except Exception as e:
        logger.error(f"Error in product_detail route: {e}")
        return render_template('errors/500.html'), 500
