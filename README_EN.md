# Capsule - B2B Moroccan Artisan Sourcing Platform

Capsule is a B2B platform specializing in sourcing authentic Moroccan artisan products, designed for professionals (hotels, decorators, boutiques).

## Overview

The Art of Moroccan Craftsmanship - Unique pieces, shaped by expert hands.

### Our Mission

Connecting Moroccan artisans with professionals worldwide by ensuring:
- **Authenticity** - 100% handmade Moroccan products
- **Ethics** - Fair trade and respect for artisans
- **Excellence** - Rigorous selection and quality control

## Environment Variables

### Required Variables (Secrets)

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | PostgreSQL connection URL |
| `SESSION_SECRET` | Secret key for Flask sessions |

### Admin Creation Variables (Secrets)

| Variable | Description |
|----------|-------------|
| `ADMIN_USERNAME` | Admin username |
| `ADMIN_PASSWORD` | Admin password |
| `ADMIN_EMAIL` | Admin email |

### Optional Variables (Contact & Social Media)

| Variable | Description |
|----------|-------------|
| `CONTACT_EMAIL` | Contact email |
| `CONTACT_PHONE` | Phone number |
| `CONTACT_WHATSAPP` | WhatsApp number |
| `CONTACT_ADDRESS` | Address |
| `SOCIAL_INSTAGRAM` | Instagram URL |
| `SOCIAL_FACEBOOK` | Facebook URL |
| `SOCIAL_TIKTOK` | TikTok URL |

## Installation and Setup

### In Development

```bash
# 1. Configure environment variables in Replit Secrets
# DATABASE_URL, SESSION_SECRET, ADMIN_USERNAME, ADMIN_PASSWORD, ADMIN_EMAIL

# 2. Initialize the database
python init_db.py --seed

# 3. Start the application
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

### Initialization Script

```bash
# Create tables only
python init_db.py

# Create tables AND add default data
python init_db.py --seed
```

## Project Structure

```
capsule/
├── app.py                  # Main Flask application
├── main.py                 # Gunicorn entry point
├── init_db.py              # Database initialization script
├── routes/                 # Flask Blueprints
│   ├── main.py            # Main routes
│   ├── catalogue.py       # Catalogue routes
│   ├── business.py        # B2B routes
│   ├── admin.py           # Admin panel
│   └── auth.py            # Authentication
├── models/                 # SQLAlchemy models
├── services/               # Business logic
├── utils/                  # Utilities
├── templates/              # HTML templates (Jinja2)
└── static/                 # CSS, JS, Images
```

## Available Pages

### Main Pages
- **Home** (`/`) - Presentation and key figures
- **Catalogue** (`/catalogue`) - Product listing
- **About** (`/a-propos`) - Mission and values
- **Contact** (`/contact`) - Contact form

### Business Pages (B2B)
- **Services** (`/services`) - Sourcing services
- **Partnerships** (`/partenariats`) - Become a partner
- **Our Process** (`/processus`) - Methodology
- **FAQ** (`/faq`) - Frequently asked questions

### Admin Panel (`/admin`)
- Dashboard with statistics
- Product and category management
- Services and FAQ management
- Site configuration (contact, social media)
- SEO settings per page

## Supported Social Networks

The following networks can be configured in admin:
- **WhatsApp** - Number for direct contacts
- **Facebook** - Facebook page
- **Instagram** - Instagram profile
- **TikTok** - TikTok account

## Tech Stack

- **Backend**: Python Flask with Blueprints
- **Database**: PostgreSQL with SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript
- **Templating**: Jinja2
- **Server**: Gunicorn
- **Authentication**: Flask-Login

## Design

### Color Palette
- Primary: `#8B7355` (golden brown)
- Accent: `#b8824e` (golden beige)
- Backgrounds: `#faf7f2`, `#f5ede1`

---

2025 Capsule - All rights reserved

[Version Francaise](README.md)
