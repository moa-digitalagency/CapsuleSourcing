from app import app, db
import logging
import os
import traceback

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def init_database():
    """Initialize database with error handling."""
    try:
        from init_db import seed_all_data, seed_page_content
        import models.database
        from models.database import User
        
        db.create_all()
        logger.info("Database tables created")
        
        try:
            seed_all_data()
            seed_page_content()
            logger.info("Database seeding completed")
        except Exception as e:
            logger.warning(f"Seeding warning (may be normal if data exists): {e}")
            db.session.rollback()
        
        admin_username = os.environ.get('ADMIN_USERNAME')
        admin_email = os.environ.get('ADMIN_EMAIL')
        admin_password = os.environ.get('ADMIN_PASSWORD')
        
        if admin_username and admin_email and admin_password:
            try:
                admin_user = User.query.filter_by(username=admin_username).first()
                if not admin_user:
                    admin_user = User(
                        username=admin_username,
                        email=admin_email,
                        is_admin=True
                    )
                    admin_user.set_password(admin_password)
                    db.session.add(admin_user)
                    db.session.commit()
                    logger.info(f"Admin user '{admin_username}' created from environment variables")
                else:
                    admin_user.email = admin_email
                    admin_user.is_admin = True
                    admin_user.set_password(admin_password)
                    db.session.commit()
                    logger.info(f"Admin user '{admin_username}' updated from environment variables")
            except Exception as e:
                logger.warning(f"Admin user setup warning: {e}")
                db.session.rollback()
                
    except Exception as e:
        logger.error(f"Database initialization error: {e}")
        logger.error(traceback.format_exc())
        raise

with app.app_context():
    init_database()

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
