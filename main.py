from app import app, db
import logging

with app.app_context():
    import models.database
    db.create_all()
    logging.info("Database tables created")

from routes import main_bp, catalogue_bp, business_bp
from routes.admin import admin_bp
from routes.auth import auth_bp

app.register_blueprint(main_bp)
app.register_blueprint(catalogue_bp)
app.register_blueprint(business_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
