# Capsule - Plateforme B2B de Sourcing Artisanat Marocain

## Vue d'ensemble
Capsule est une plateforme B2B de sourcing de produits artisanaux marocains authentiques. Le site met en valeur le savoir-faire traditionnel marocain a travers une selection de produits artisanaux de qualite, destine aux professionnels (hotels, decorateurs, boutiques).

## Architecture du Projet

### Stack Technique
- **Backend**: Python Flask avec Blueprints
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Templating**: Jinja2
- **Base de donnees**: PostgreSQL avec SQLAlchemy ORM
- **Authentification**: Replit Auth (OAuth2)
- **Architecture**: MVC avec services

### Structure des Fichiers
```
.
├── app.py                  # Application Flask principale, config DB
├── main.py                 # Point d'entree gunicorn, registration des blueprints
├── replit_auth.py          # Authentification Replit OAuth2
├── routes/                 # Blueprints Flask
│   ├── __init__.py        # Export des blueprints
│   ├── main.py            # Routes principales (index, about, contact)
│   ├── catalogue.py       # Routes catalogue et produits
│   ├── business.py        # Routes B2B (services, partenariats, faq)
│   └── admin.py           # Panel d'administration complet
├── models/                 # Modeles de donnees
│   ├── __init__.py        # Export de tous les modeles
│   ├── product.py         # Classes Product et Category (donnees statiques)
│   └── database.py        # Modeles SQLAlchemy pour la DB
├── services/               # Logique metier
│   ├── __init__.py
│   └── product_service.py # Service de gestion des produits
├── utils/                  # Utilitaires
│   ├── __init__.py
│   └── helpers.py         # Fonctions utilitaires
├── templates/              # Templates HTML
│   ├── base.html          # Template de base
│   ├── index.html         # Page d'accueil
│   ├── catalogue.html     # Page catalogue
│   ├── product.html       # Page produit detaillee
│   ├── about.html         # Page a propos
│   ├── contact.html       # Page contact
│   ├── services.html      # Page services B2B
│   ├── partenariats.html  # Page partenariats
│   ├── processus.html     # Page processus de travail
│   ├── faq.html           # Page FAQ
│   ├── 403.html           # Page acces non autorise
│   └── admin/             # Templates admin
│       ├── base.html      # Layout admin avec sidebar
│       ├── dashboard.html # Tableau de bord
│       ├── products.html  # Liste des produits
│       ├── product_form.html
│       ├── categories.html
│       ├── category_form.html
│       ├── services.html
│       ├── service_form.html
│       ├── faqs.html
│       ├── faq_form.html
│       ├── partnerships.html
│       ├── partnership_form.html
│       ├── process_steps.html
│       ├── process_step_form.html
│       ├── testimonials.html
│       ├── testimonial_form.html
│       ├── homepage.html  # Edition hero et stats
│       ├── seo.html       # Parametres SEO par page
│       ├── settings.html  # Infos de contact
│       └── users.html     # Gestion des utilisateurs
├── static/
│   ├── css/
│   │   └── style.css      # Styles CSS
│   ├── js/
│   │   └── script.js      # Scripts JavaScript
│   ├── images/            # Images du site
│   └── uploads/           # Images uploadees via admin
└── attached_assets/        # Assets fournis par l'utilisateur
```

## Modeles de Donnees (SQLAlchemy)

### Modeles d'authentification
- **User**: Utilisateurs avec is_admin flag
- **OAuth**: Tokens OAuth pour Replit Auth

### Modeles de contenu
- **CategoryDB**: Categories de produits
- **ProductDB**: Produits avec images, description, materiaux
- **Service**: Services B2B
- **PartnershipType**: Types de partenariats
- **ProcessStep**: Etapes du processus de travail
- **FAQ**: Questions frequentes
- **Testimonial**: Temoignages clients

### Modeles de configuration
- **HeroSection**: Section hero de la page d'accueil
- **HomepageStats**: Statistiques (artisans, produits, partenaires, pays)
- **SEOSettings**: Meta tags par page
- **ContactInfo**: Informations de contact

## Panel d'Administration

### Acces
- URL: `/admin`
- Authentification requise via Replit Auth
- Droit admin requis (is_admin=True sur le User)

### Fonctionnalites
1. **Dashboard** - Vue d'ensemble avec statistiques
2. **Produits** - CRUD complet avec upload d'images
3. **Categories** - Gestion des categories
4. **Services** - Services B2B editables
5. **Partenariats** - Types de partenariats
6. **Processus** - Etapes du processus de travail
7. **FAQ** - Questions/reponses
8. **Temoignages** - Avis clients avec photos
9. **Page d'accueil** - Hero section et statistiques
10. **SEO** - Meta tags par page
11. **Parametres** - Infos de contact et reseaux sociaux
12. **Utilisateurs** - Gestion des droits admin

### Upload d'Images
- Formats acceptes: PNG, JPG, JPEG, GIF, WEBP, SVG
- Stockage: `/static/uploads/`
- Taille max: 16 MB

## Routes et Blueprints

### main_bp (routes/main.py)
- `GET /` - Page d'accueil
- `GET /a-propos` - Page a propos
- `GET /contact` - Page contact
- `POST /contact` - Soumission formulaire

### catalogue_bp (routes/catalogue.py)
- `GET /catalogue` - Liste des produits
- `GET /produit/<id>` - Detail d'un produit

### business_bp (routes/business.py)
- `GET /services` - Page services
- `GET /partenariats` - Page partenariats
- `GET /processus` - Page processus
- `GET /faq` - Page FAQ

### admin_bp (routes/admin.py)
- `GET /admin/` - Dashboard
- `GET/POST /admin/products` - Produits
- `GET/POST /admin/categories` - Categories
- `GET/POST /admin/services` - Services
- `GET/POST /admin/partnerships` - Partenariats
- `GET/POST /admin/process` - Processus
- `GET/POST /admin/faqs` - FAQ
- `GET/POST /admin/testimonials` - Temoignages
- `GET/POST /admin/homepage` - Page d'accueil
- `GET/POST /admin/seo` - SEO
- `GET/POST /admin/settings` - Parametres
- `GET /admin/users` - Utilisateurs

### auth (replit_auth.py)
- `GET /auth/login` - Connexion Replit
- `GET /auth/logout` - Deconnexion
- `GET /auth/error` - Erreur d'authentification

## Variables d'Environnement

### Requises
- `DATABASE_URL` - URL PostgreSQL
- `SESSION_SECRET` - Cle secrete pour les sessions
- `REPL_ID` - ID du Repl (automatique)

### Optionnelles
- `ADMIN_EMAILS` - Liste d'emails separes par virgules qui seront automatiquement admin a leur premiere connexion

### Bootstrap Admin
Le premier utilisateur a se connecter devient automatiquement admin. Alternativement, vous pouvez definir la variable `ADMIN_EMAILS` avec une liste d'emails qui seront promus admin a leur premiere connexion.

## Design

### Palette de Couleurs
- **Primaire**: #8B7355 (marron dore)
- **Texte**: #1a1a1a, #333, #666
- **Backgrounds**: #f5f5f5, #fff, #fafafa
- **Accent**: #8B7355

### Typographie
- **Admin**: System fonts (-apple-system, Segoe UI, Roboto)
- **Site**: Georgia (titres), System fonts (corps)

## Developpement

### Lancer l'application
```bash
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

### Premier admin
1. Se connecter via Replit Auth
2. Modifier directement en DB: `UPDATE users SET is_admin = true WHERE id = 'votre-id'`
3. Ou utiliser l'admin existant pour promouvoir d'autres utilisateurs

## Modifications Recentes

### 26/11/2024: Panel d'Administration Complet
- Integration PostgreSQL avec SQLAlchemy ORM
- Authentification Replit OAuth2
- Panel admin complet avec sidebar navigation
- CRUD pour tous les types de contenu
- Upload d'images avec stockage local
- Gestion des utilisateurs et droits admin
- Parametres SEO par page
- Edition de la page d'accueil (hero, stats)
- Gestion des informations de contact

### 26/11/2024: Navigation, WhatsApp et Responsive
- Menu hamburger responsive pour mobile/tablet
- Integration WhatsApp pour le formulaire contact
- Favicon SVG ajoute

### 26/11/2024: Architecture B2B et restructuration
- Restructuration complete du backend avec Flask Blueprints
- Pages B2B: Services, Partenariats, FAQ
- Menu avec dropdown "Entreprise"
