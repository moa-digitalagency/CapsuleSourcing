from datetime import datetime
from flask_login import UserMixin
from sqlalchemy import UniqueConstraint
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=True)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)


class CategoryDB(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    icon = db.Column(db.String(50), nullable=True)
    order = db.Column(db.Integer, default=0)
    products = db.relationship('ProductDB', backref='category_rel', lazy=True)


class ProductDB(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    category_id = db.Column(db.String(50), db.ForeignKey('categories.id'), nullable=False)
    description = db.Column(db.Text, nullable=True)
    details = db.Column(db.Text, nullable=True)
    dimensions = db.Column(db.String(200), nullable=True)
    material = db.Column(db.String(200), nullable=True)
    image = db.Column(db.String(500), nullable=True)
    is_featured = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category_id,
            'description': self.description,
            'details': self.details,
            'dimensions': self.dimensions,
            'material': self.material,
            'image': self.image
        }


class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    icon = db.Column(db.String(50), nullable=True)
    order = db.Column(db.Integer, default=0)


class PartnershipType(db.Model):
    __tablename__ = 'partnership_types'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    benefits = db.Column(db.Text, nullable=True)
    order = db.Column(db.Integer, default=0)


class ProcessStep(db.Model):
    __tablename__ = 'process_steps'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    order = db.Column(db.Integer, default=0)


class FAQ(db.Model):
    __tablename__ = 'faqs'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.Text, nullable=True)
    order = db.Column(db.Integer, default=0)


class Testimonial(db.Model):
    __tablename__ = 'testimonials'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author_name = db.Column(db.String(200), nullable=False)
    author_title = db.Column(db.String(200), nullable=True)
    author_image = db.Column(db.String(500), nullable=True)
    order = db.Column(db.Integer, default=0)


class PageContent(db.Model):
    __tablename__ = 'page_contents'
    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.String(50), nullable=False)
    section = db.Column(db.String(100), nullable=False)
    key = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Text, nullable=True)
    __table_args__ = (UniqueConstraint('page', 'section', 'key', name='uq_page_section_key'),)


class SiteSettings(db.Model):
    __tablename__ = 'site_settings'
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(100), unique=True, nullable=False)
    value = db.Column(db.Text, nullable=True)
    category = db.Column(db.String(50), default='general')


class SEOSettings(db.Model):
    __tablename__ = 'seo_settings'
    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.String(50), unique=True, nullable=False)
    meta_title = db.Column(db.String(200), nullable=True)
    meta_description = db.Column(db.Text, nullable=True)
    meta_keywords = db.Column(db.Text, nullable=True)
    og_title = db.Column(db.String(200), nullable=True)
    og_description = db.Column(db.Text, nullable=True)
    og_image = db.Column(db.String(500), nullable=True)


class HomepageStats(db.Model):
    __tablename__ = 'homepage_stats'
    id = db.Column(db.Integer, primary_key=True)
    artisans = db.Column(db.Integer, default=50)
    products = db.Column(db.Integer, default=200)
    partners = db.Column(db.Integer, default=35)
    countries = db.Column(db.Integer, default=12)


class HeroSection(db.Model):
    __tablename__ = 'hero_sections'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), default="L'Art du Savoir-Faire Marocain")
    subtitle = db.Column(db.String(500), default="Des pieces uniques, faconnees par des mains expertes")
    button_text = db.Column(db.String(100), default="Decouvrir la Collection")
    main_image = db.Column(db.String(500), nullable=True)
    card1_title = db.Column(db.String(100), default="Ebenisterie")
    card1_subtitle = db.Column(db.String(200), default="Le travail du bois traditionnel")
    card1_image = db.Column(db.String(500), nullable=True)
    card1_link = db.Column(db.String(50), default="mobilier")
    card2_title = db.Column(db.String(100), default="Fibres Naturelles")
    card2_subtitle = db.Column(db.String(200), default="Vannerie et tissage artisanal")
    card2_image = db.Column(db.String(500), nullable=True)
    card2_link = db.Column(db.String(50), default="textile")


class ContactInfo(db.Model):
    __tablename__ = 'contact_info'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), default="contact@capsule-maroc.com")
    phone = db.Column(db.String(50), default="+212 XX XX XX XX")
    whatsapp = db.Column(db.String(50), nullable=True)
    address = db.Column(db.Text, nullable=True)
    instagram = db.Column(db.String(200), nullable=True)
    facebook = db.Column(db.String(200), nullable=True)
    tiktok = db.Column(db.String(200), nullable=True)
