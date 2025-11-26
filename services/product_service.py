class ProductService:
    def __init__(self):
        pass
    
    def get_all_products(self):
        from models.database import ProductDB
        products = ProductDB.query.order_by(ProductDB.order).all()
        return [p.to_dict() for p in products]
    
    def get_featured_products(self, limit=6):
        from models.database import ProductDB
        products = ProductDB.query.filter_by(is_featured=True).order_by(ProductDB.order).limit(limit).all()
        return [p.to_dict() for p in products]
    
    def get_product_by_id(self, product_id):
        from models.database import ProductDB
        product = ProductDB.query.get(product_id)
        return product.to_dict() if product else None
    
    def get_categories(self):
        from models.database import CategoryDB
        categories = CategoryDB.query.order_by(CategoryDB.order).all()
        result = [{'id': 'all', 'name': 'Tous les produits', 'icon': None}]
        for cat in categories:
            result.append({'id': cat.id, 'name': cat.name, 'icon': cat.icon})
        return result
    
    def get_products_by_category(self, category_id):
        from models.database import ProductDB
        if category_id == 'all':
            products = ProductDB.query.order_by(ProductDB.order).all()
        else:
            products = ProductDB.query.filter_by(category_id=category_id).order_by(ProductDB.order).all()
        return [p.to_dict() for p in products]
    
    def get_related_products(self, product, limit=4):
        from models.database import ProductDB
        related = ProductDB.query.filter(
            ProductDB.category_id == product.get('category'),
            ProductDB.id != product.get('id')
        ).order_by(ProductDB.order).limit(limit).all()
        return [p.to_dict() for p in related]
