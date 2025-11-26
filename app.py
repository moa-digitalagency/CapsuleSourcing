import os
import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from sqlalchemy.orm import DeclarativeBase
from werkzeug.middleware.proxy_fix import ProxyFix

logging.basicConfig(level=logging.DEBUG)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
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


@login_manager.user_loader
def load_user(user_id):
    from models.database import User
    return User.query.get(int(user_id))


@app.context_processor
def inject_contact_info():
    from models.database import ContactInfo
    contact = ContactInfo.query.first()
    return dict(contact_info=contact)


@app.context_processor
def inject_seo():
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
