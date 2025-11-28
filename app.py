import os
import logging
import traceback
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()

app = Flask(__name__)

session_secret = os.environ.get("SESSION_SECRET")
if not session_secret:
    logger.warning("SESSION_SECRET not set, using fallback (not recommended for production)")
    session_secret = "dev-fallback-secret-change-in-production"
app.secret_key = session_secret

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

database_url = os.environ.get("DATABASE_URL")
if not database_url:
    logger.error("DATABASE_URL not set! Application will not work properly.")
else:
    logger.info(f"Database configured: {database_url[:30]}...")

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    'pool_pre_ping': True,
    "pool_recycle": 300,
}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Veuillez vous connecter pour acceder a cette page.'


@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal Server Error: {error}")
    logger.error(traceback.format_exc())
    db.session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled Exception: {e}")
    logger.error(traceback.format_exc())
    db.session.rollback()
    return render_template('errors/500.html'), 500


@login_manager.user_loader
def load_user(user_id):
    from models.database import User
    return User.query.get(int(user_id))


@app.context_processor
def inject_contact_info():
    try:
        from models.database import ContactInfo
        contact = ContactInfo.query.first()
        return dict(contact_info=contact)
    except Exception as e:
        logger.warning(f"Error loading contact info: {e}")
        return dict(contact_info=None)


@app.context_processor
def inject_seo():
    try:
        from flask import request
        from models.database import SEOSettings
        
        page_mapping = {
            'main.index': 'index',
            'catalogue.catalogue': 'catalogue',
            'catalogue.product_detail': 'catalogue',
            'main.about': 'about',
            'main.contact': 'contact',
            'business.services': 'services',
            'business.partenariats': 'partenariats',
            'business.processus': 'processus',
            'business.faq': 'faq',
            'auth.login': 'index',
            'auth.register': 'index',
        }
        
        page_name = page_mapping.get(request.endpoint)
        seo = None
        if page_name:
            seo = SEOSettings.query.filter_by(page=page_name).first()
        
        return dict(seo=seo)
    except Exception as e:
        logger.warning(f"Error loading SEO settings: {e}")
        return dict(seo=None)
