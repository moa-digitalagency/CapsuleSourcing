# Capsule - Plateforme B2B de Sourcing Artisanat Marocain

## Vue d'ensemble
Capsule est une plateforme B2B de sourcing de produits artisanaux marocains authentiques. Le site met en valeur le savoir-faire traditionnel marocain a travers une selection de produits artisanaux de qualite, destine aux professionnels (hotels, decorateurs, boutiques).

## Architecture du Projet

### Stack Technique
- **Backend**: Python Flask avec Blueprints
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Templating**: Jinja2
- **Stockage**: Donnees en memoire (models/product.py)
- **Architecture**: MVC avec services

### Structure des Fichiers
```
.
├── app.py                  # Application Flask principale
├── main.py                 # Point d'entree gunicorn
├── routes/                 # Blueprints Flask
│   ├── __init__.py        # Export des blueprints
│   ├── main.py            # Routes principales (index, about, contact)
│   ├── catalogue.py       # Routes catalogue et produits
│   └── business.py        # Routes B2B (services, partenariats, faq)
├── models/                 # Modeles de donnees
│   ├── __init__.py
│   └── product.py         # Classes Product et Category
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
│   └── faq.html           # Page FAQ
├── static/
│   ├── css/
│   │   └── style.css      # Styles CSS
│   ├── js/
│   │   └── script.js      # Scripts JavaScript
│   └── images/            # Images du site
└── attached_assets/        # Assets fournis par l'utilisateur
```

## Fonctionnalites

### Pages Principales
1. **Accueil** (`/`)
   - Hero section avec presentation de l'artisanat marocain
   - Section chiffres cles (stats business)
   - Nos Creations Phares avec grid showcase
   - Valeurs: Authenticite, Ethique, Excellence
   - Apercu du processus de travail
   - Call-to-action B2B

2. **Catalogue** (`/catalogue`)
   - Filtres par categorie (Laiton, Ceramique, Textile, Mobilier, Luminaires, Bijoux, Decoration)
   - Grille de produits responsive
   - Navigation par categories (sans emojis)

3. **Produit** (`/produit/<id>`)
   - Details complets du produit
   - Caracteristiques techniques
   - Produits similaires
   - Bouton de demande de devis

4. **A Propos** (`/a-propos`)
   - Mission et valeurs de Capsule
   - Expertise en sourcing
   - Engagement qualite et commerce equitable

5. **Contact** (`/contact`)
   - Formulaire de contact
   - Informations de contact
   - Horaires d'ouverture

### Pages B2B
6. **Services** (`/services`)
   - Services de sourcing
   - Personnalisation
   - Controle qualite
   - Logistique

7. **Partenariats** (`/partenariats`)
   - Types de partenaires (Hotels, Decorateurs, Boutiques)
   - Avantages du partenariat
   - Formulaire de demande

8. **FAQ** (`/faq`)
   - Questions frequentes sur le sourcing
   - Processus de commande
   - Delais et livraison

### Categories de Produits
- **Laiton**: Ex-votos, mobiles, plateaux, pateres, soliflores, bougeoirs
- **Ceramique & Poterie**: Poteries terre cuite, vaisselle artisanale
- **Textile & Tissage**: Tapis, poufs, coussins, paniers
- **Mobilier**: Meubles en bois et tissages
- **Luminaires**: Appliques murales en laiton
- **Bijoux**: Bracelets Maayaz (sfifa traditionnelle)
- **Decoration**: Miroirs, cadres, trophees

## Design

### Palette de Couleurs
- **Primaire**: #b8824e (beige dore)
- **Terre cuite**: #c86640
- **Cuivre**: #b87333
- **Or**: #d4af37
- **Backgrounds**: #faf7f2, #f5ede1
- **Texte**: #2c2416

### Typographie
- **Titres**: Georgia (serif)
- **Corps**: System fonts (sans-serif)

### Responsive
- Desktop: > 968px
- Tablet: 640px - 968px
- Mobile: < 640px

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

## Developpement

### Lancer l'application
```bash
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

### Ajouter des Produits
Modifier le fichier `models/product.py` et ajouter des entrees dans la fonction `get_all_products()`.

### Ajouter des Images
Placer les images dans `static/images/` et mettre a jour les chemins dans les produits.

## Modifications Recentes

### 26/11/2024: Architecture B2B et restructuration
- Restructuration complete du backend avec Flask Blueprints
- Separation en dossiers: routes/, models/, services/, utils/
- Suppression de tous les emojis (remplacements par icones SVG)
- Ajout des pages B2B: Services, Partenariats, FAQ
- Menu avec dropdown "Entreprise"
- Section chiffres cles sur la page d'accueil
- Section processus de travail
- Expansion des sections valeurs et creations phares
- Navigation professionnelle orientee B2B

### 26/11/2024: Refonte design minimaliste
- Design epure avec palette de couleurs terre
- Typographie elegante (Georgia serif)
- Animations au scroll avec IntersectionObserver
- Navigation fixe avec effet de transparence

### 25/11/2024: Creation initiale
- Structure Flask complete
- 18 produits artisanaux marocains
- 8 categories de produits
- Design inspire de l'artisanat marocain
- Pages responsive et modernes
- Formulaire de contact fonctionnel

## Ameliorations Futures
1. Integrer une base de donnees PostgreSQL
2. Ajouter un systeme d'administration
3. Implementer la recherche de produits
4. Ajouter une galerie Instagram
5. Integrer une newsletter
6. Optimiser le SEO
7. Ajouter l'authentification pour les partenaires B2B
