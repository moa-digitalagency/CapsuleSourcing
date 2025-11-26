# Capsule - Plateforme B2B de Sourcing Artisanat Marocain

## Vue d'ensemble
Capsule est une plateforme B2B de sourcing de produits artisanaux marocains authentiques. Le site met en valeur le savoir-faire traditionnel marocain a travers une selection de produits artisanaux de qualite, destine aux professionnels (hotels, decorateurs, boutiques).

## Architecture du Projet

### Stack Technique
- **Backend**: Python Flask avec Blueprints
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Templating**: Jinja2
- **Base de donnees**: PostgreSQL avec SQLAlchemy ORM
- **Authentification**: Python Flask-Login (username/password)
- **Traitement d'images**: Pillow (rognage et redimensionnement)
- **Architecture**: MVC avec services

### Structure des Fichiers
```
.
├── app.py                  # Application Flask principale, config DB
├── main.py                 # Point d'entree gunicorn, registration des blueprints
├── routes/                 # Blueprints Flask
│   ├── __init__.py        # Export des blueprints
│   ├── main.py            # Routes principales (index, about, contact)
│   ├── catalogue.py       # Routes catalogue et produits
│   ├── business.py        # Routes B2B (services, partenariats, faq)
│   ├── admin.py           # Panel d'administration complet
│   └── auth.py            # Authentification Python (login/register/logout)
├── models/                 # Modeles de donnees
│   ├── __init__.py        # Export de tous les modeles
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
- **User**: Utilisateurs avec username, email, password_hash et is_admin flag

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
- **ContactInfo**: Informations de contact et reseaux sociaux

## Reseaux Sociaux

### Configuration
Les reseaux sociaux sont configurables dans `/admin/settings` via le modele ContactInfo:

| Reseau | Champ | Format |
|--------|-------|--------|
| WhatsApp | `whatsapp` | Numero (+212 6 XX XX XX XX) |
| Facebook | `facebook` | URL (https://facebook.com/...) |
| Instagram | `instagram` | URL (https://instagram.com/...) |
| TikTok | `tiktok` | URL (https://tiktok.com/@...) |

### Affichage
Les icones s'affichent automatiquement dans le footer (`templates/base.html`) lorsque les liens sont configures.

## Panel d'Administration

### Acces
- URL: `/admin`
- Authentification requise via login/password Python
- Droit admin requis (is_admin=True sur le User)
- Le premier utilisateur inscrit devient automatiquement admin

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

### auth_bp (routes/auth.py)
- `GET /auth/login` - Page de connexion
- `POST /auth/login` - Soumission connexion
- `GET /auth/register` - Page d'inscription
- `POST /auth/register` - Soumission inscription
- `GET /auth/logout` - Deconnexion

## Variables d'Environnement

### Requises
- `DATABASE_URL` - URL PostgreSQL
- `SESSION_SECRET` - Cle secrete pour les sessions

### Bootstrap Admin
Le premier utilisateur a s'inscrire devient automatiquement admin. Utilisez la gestion des utilisateurs dans l'admin pour promouvoir d'autres utilisateurs.

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
1. S'inscrire via /auth/register (le premier utilisateur est automatiquement admin)
2. Ou utiliser l'admin existant pour promouvoir d'autres utilisateurs via /admin/users

## Modifications Recentes

### 26/11/2025: Produits Vedettes et Gestion Hero
- Bouton etoile pour mettre/retirer des produits en vedette dans l'admin
- Section vedette sur l'accueil affiche les produits marques comme vedettes
- Selection de produits du catalogue pour les images du hero
- Bouton supprimer pour chaque produit dans l'admin
- Badge "VEDETTE" visible sur les produits en vedette dans l'admin

### 26/11/2025: Catalogue Galerie Simplifie
- Nouveau format galerie pour le catalogue avec numerotation des produits (#1, #2, etc.)
- Bouton WhatsApp "Ca m'interesse" sur chaque produit qui envoie le lien du produit
- 428 nouvelles images de produits ajoutees depuis le fichier zip fourni
- ProductService mis a jour pour lire depuis la base de donnees PostgreSQL
- Admin panel simplifie pour gerer les produits en mode galerie
- Suppression des categories et filtres pour un affichage galerie simple
- Images stockees dans `/static/images/products/`

### 26/11/2025: Section Vedette Redesign
- Nouvelle mise en page Section Vedette: 1 bloc principal a gauche + 4 cartes produits a droite (grille 2x2)
- Modele FeaturedHighlight avec 5 slots: slot 1 = bloc principal, slots 2-5 = cartes produits
- Champs editables: image, titre, sous-titre, badge, description, lien, texte du lien
- Gestion complete dans /admin/featured-highlights avec distinction visuelle bloc principal vs cartes
- CSS responsive: grille colonne unique sur tablet (<=1024px), cartes en colonne unique sur mobile (<=640px)
- Seeding automatique des 5 slots avec donnees par defaut si absentes

### 26/11/2025: Systeme de Contenu Dynamique des Pages
- Nouveau modele PageContent pour stocker tous les textes par page/section/cle
- Templates mis a jour pour charger le contenu depuis la base de donnees
- Nouvelle section admin "Textes des Pages" dans /admin/page-content
- Service content_service.py pour simplifier la recuperation du contenu
- Script init_db.py etendu pour initialiser tout le contenu par defaut en francais
- Contenu editable: titres, sous-titres, descriptions, boutons, sections, CTA
- Pages couvertes: index, about, services, contact, catalogue, faq, partenariats, processus
- Correction du bug Jinja2 avec la section 'values' (renommee en 'our_values')

### 26/11/2025: Migration vers Authentification Python Native
- Remplacement de Replit Auth par Flask-Login avec username/password
- Nouveau modele User avec password_hash
- Routes /auth/login, /auth/register, /auth/logout
- Templates de connexion et inscription stylises
- Correction du bug de soulignement dans le header (dropdown Entreprise)
- Ajout de WhatsApp dans le footer avec liens dynamiques
- Liens directs tel:, mailto:, wa.me pour tous les contacts
- Traitement d'images avec Pillow (rognage et redimensionnement)
- Endpoint /admin/upload-with-crop pour upload avec rognage
- Suppression des fichiers inutilises (products.py, models/product.py, replit_auth.py)
- Base de donnees PostgreSQL verifiee et fonctionnelle

### 26/11/2024: Panel d'Administration Complet
- Integration PostgreSQL avec SQLAlchemy ORM
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
