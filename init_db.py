#!/usr/bin/env python3
"""
Database Initialization Script for Capsule

This script initializes the database with all required tables and
optionally seeds default data. Run this script to set up the database
before starting the application for the first time.

Usage:
    python init_db.py [--seed]
    
Options:
    --seed    Add default data (admin user, sample categories, etc.)
"""
import os
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def init_database():
    """Initialize all database tables."""
    from app import app, db
    
    with app.app_context():
        import models.database
        
        logger.info("Creating database tables...")
        db.create_all()
        logger.info("Database tables created successfully!")
        
        return True


def seed_default_data():
    """Seed the database with default data."""
    from app import app, db
    from models.database import (
        User, ContactInfo, HeroSection, HomepageStats, 
        SEOSettings, CategoryDB
    )
    from werkzeug.security import generate_password_hash
    
    admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
    admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123')
    admin_email = os.environ.get('ADMIN_EMAIL', 'admin@capsule-maroc.com')
    
    with app.app_context():
        if User.query.filter_by(is_admin=True).first():
            logger.info("Admin user already exists, skipping user creation.")
        else:
            admin = User(
                username=admin_username,
                email=admin_email,
                password_hash=generate_password_hash(admin_password),
                first_name="Admin",
                last_name="Capsule",
                is_admin=True
            )
            db.session.add(admin)
            logger.info(f"Created admin user (username: {admin_username})")
        
        contact = ContactInfo.query.first()
        if not contact:
            contact = ContactInfo(
                email="contact@capsule-maroc.com",
                phone="+212 5 24 43 XX XX",
                whatsapp="+212 6 61 XX XX XX",
                address="Quartier Industriel, Marrakech, Maroc",
                instagram="https://instagram.com/capsule.maroc",
                facebook="https://facebook.com/capsulemaroc",
                linkedin="https://linkedin.com/company/capsule-maroc",
                twitter="https://twitter.com/capsulemaroc",
                youtube="https://youtube.com/@capsulemaroc",
                tiktok="https://tiktok.com/@capsulemaroc",
                pinterest="https://pinterest.com/capsulemaroc"
            )
            db.session.add(contact)
            logger.info("Created default contact info with social networks")
        else:
            if not contact.instagram:
                contact.instagram = "https://instagram.com/capsule.maroc"
            if not contact.facebook:
                contact.facebook = "https://facebook.com/capsulemaroc"
            if not contact.linkedin:
                contact.linkedin = "https://linkedin.com/company/capsule-maroc"
            if not contact.whatsapp:
                contact.whatsapp = "+212 6 61 XX XX XX"
            if not contact.twitter:
                contact.twitter = "https://twitter.com/capsulemaroc"
            if not contact.youtube:
                contact.youtube = "https://youtube.com/@capsulemaroc"
            if not contact.tiktok:
                contact.tiktok = "https://tiktok.com/@capsulemaroc"
            if not contact.pinterest:
                contact.pinterest = "https://pinterest.com/capsulemaroc"
            logger.info("Updated contact info with social networks")
        
        if not HeroSection.query.first():
            hero = HeroSection()
            db.session.add(hero)
            logger.info("Created default hero section")
        
        if not HomepageStats.query.first():
            stats = HomepageStats()
            db.session.add(stats)
            logger.info("Created default homepage stats")
        
        pages = ['index', 'catalogue', 'about', 'contact', 'services', 'partenariats', 'processus', 'faq']
        for page in pages:
            if not SEOSettings.query.filter_by(page=page).first():
                seo = SEOSettings(page=page)
                db.session.add(seo)
        logger.info("Created SEO settings for all pages")
        
        default_categories = [
            {'id': 'mobilier', 'name': 'Mobilier', 'icon': 'home', 'order': 1},
            {'id': 'textile', 'name': 'Textile', 'icon': 'layers', 'order': 2},
            {'id': 'ceramique', 'name': 'Ceramique', 'icon': 'coffee', 'order': 3},
            {'id': 'cuir', 'name': 'Cuir', 'icon': 'briefcase', 'order': 4},
            {'id': 'metal', 'name': 'Metal', 'icon': 'tool', 'order': 5},
            {'id': 'bois', 'name': 'Bois', 'icon': 'box', 'order': 6},
        ]
        
        for cat in default_categories:
            if not CategoryDB.query.get(cat['id']):
                category = CategoryDB(**cat)
                db.session.add(category)
        logger.info("Created default categories")
        
        db.session.commit()
        logger.info("Default data seeded successfully!")
        
        return True


def main():
    """Main entry point."""
    seed = '--seed' in sys.argv
    
    logger.info("=" * 50)
    logger.info("Capsule Database Initialization")
    logger.info("=" * 50)
    
    if not os.environ.get('DATABASE_URL'):
        logger.error("DATABASE_URL environment variable is not set!")
        logger.error("Please set DATABASE_URL before running this script.")
        sys.exit(1)
    
    try:
        if init_database():
            logger.info("Database initialized successfully!")
            
            if seed:
                logger.info("")
                logger.info("Seeding default data...")
                seed_default_data()
            else:
                logger.info("")
                logger.info("Tip: Run with --seed to add default data")
    
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        sys.exit(1)
    
    logger.info("")
    logger.info("=" * 50)
    logger.info("Initialization complete!")
    logger.info("=" * 50)


if __name__ == '__main__':
    main()
