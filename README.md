# Capsule - Plateforme B2B de Sourcing Artisanat Marocain

Capsule est une plateforme B2B specialisee dans le sourcing de produits artisanaux marocains authentiques, destinee aux professionnels (hotels, decorateurs, boutiques).

## Presentation

L'Art du Savoir-Faire Marocain - Des pieces uniques, faconnees par des mains expertes.

### Notre Mission

Connecter les artisans marocains aux professionnels du monde entier en garantissant:
- **Authenticite** - Produits 100% artisanaux marocains
- **Ethique** - Commerce equitable et respect des artisans
- **Excellence** - Selection rigoureuse et controle qualite

## Variables d'Environnement

### Variables Obligatoires

| Variable | Description | Exemple |
|----------|-------------|---------|
| `DATABASE_URL` | URL de connexion PostgreSQL | `postgresql://user:pass@host:5432/dbname` |
| `SESSION_SECRET` | Cle secrete pour les sessions Flask | `your-secret-key-here` |

### Variables PostgreSQL (fournies automatiquement avec DATABASE_URL)

| Variable | Description |
|----------|-------------|
| `PGHOST` | Hote de la base de donnees |
| `PGPORT` | Port de la base de donnees (defaut: 5432) |
| `PGUSER` | Nom d'utilisateur |
| `PGPASSWORD` | Mot de passe |
| `PGDATABASE` | Nom de la base de donnees |

### Variables Optionnelles

| Variable | Description | Defaut |
|----------|-------------|--------|
| `FLASK_ENV` | Environnement Flask | `production` |
| `FLASK_DEBUG` | Mode debug | `0` |

## Installation et Lancement

### En Developpement

```bash
# 1. Configurer les variables d'environnement
export DATABASE_URL="postgresql://user:pass@localhost:5432/capsule"
export SESSION_SECRET="dev-secret-key"

# 2. Initialiser la base de donnees
python init_db.py --seed

# 3. Lancer l'application
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

### En Production

```bash
# 1. Configurer les variables d'environnement (via votre plateforme de deploiement)
# DATABASE_URL et SESSION_SECRET sont obligatoires

# 2. Initialiser la base de donnees (premiere fois seulement)
python init_db.py --seed

# 3. Lancer l'application
gunicorn --bind 0.0.0.0:5000 main:app
```

### Script d'Initialisation de la Base de Donnees

```bash
# Creer uniquement les tables
python init_db.py

# Creer les tables ET ajouter les donnees par defaut
python init_db.py --seed
```

Le script `init_db.py` cree:
- Toutes les tables de la base de donnees
- Un utilisateur admin par defaut (avec --seed)
- Les informations de contact par defaut
- Les parametres SEO pour toutes les pages
- Les categories de produits par defaut

## Categories de Produits

| Categorie | Description |
|-----------|-------------|
| Laiton | Ex-votos, mobiles, plateaux, pateres, soliflores, bougeoirs |
| Ceramique & Poterie | Poteries terre cuite, vaisselle artisanale |
| Textile & Tissage | Tapis, poufs, coussins, paniers |
| Mobilier | Meubles en bois et tissages traditionnels |
| Luminaires | Appliques murales en laiton |
| Bijoux | Bracelets Maayaz (sfifa traditionnelle) |
| Decoration | Miroirs, cadres, trophees |

## Structure du Projet

```
capsule/
├── app.py                  # Application Flask principale
├── main.py                 # Point d'entree gunicorn
├── init_db.py              # Script d'initialisation de la BDD
├── routes/                 # Blueprints Flask
│   ├── __init__.py        # Configuration des blueprints
│   ├── main.py            # Routes principales (index, about, contact)
│   ├── catalogue.py       # Routes catalogue et produits
│   ├── business.py        # Routes B2B (services, partenariats, faq)
│   ├── admin.py           # Panel d'administration
│   └── auth.py            # Authentification
├── models/                 # Modeles de donnees
│   └── database.py        # Modeles SQLAlchemy
├── services/               # Logique metier
│   └── product_service.py # Service de gestion des produits
├── utils/                  # Utilitaires
│   ├── helpers.py         # Fonctions utilitaires
│   └── image_processor.py # Traitement des images
├── templates/              # Templates HTML (Jinja2)
│   ├── admin/             # Templates panel admin
│   ├── auth/              # Templates authentification
│   └── *.html             # Pages publiques
├── static/
│   ├── css/style.css      # Styles CSS
│   ├── js/script.js       # Scripts JavaScript
│   ├── images/            # Images du site
│   └── uploads/           # Images uploadees
└── README.md
```

## Pages Disponibles

### Pages Principales
- **Accueil** (`/`) - Presentation et chiffres cles
- **Catalogue** (`/catalogue`) - Liste des produits avec filtres par categorie
- **Produit** (`/produit/<id>`) - Details d'un produit
- **A Propos** (`/a-propos`) - Mission et valeurs
- **Contact** (`/contact`) - Formulaire de contact avec WhatsApp

### Pages Business (B2B)
- **Services** (`/services`) - Services de sourcing et personnalisation
- **Partenariats** (`/partenariats`) - Devenir partenaire
- **Notre Processus** (`/processus`) - Comment nous travaillons
- **FAQ** (`/faq`) - Questions frequentes

### Authentification
- **Connexion** (`/auth/login`) - Page de connexion
- **Inscription** (`/auth/register`) - Page d'inscription
- **Deconnexion** (`/auth/logout`) - Deconnexion

### Panel d'Administration (`/admin`)
- Dashboard avec statistiques
- Gestion des produits et categories
- Gestion des services et FAQ
- Gestion des partenariats et temoignages
- Configuration du site (contact, reseaux sociaux)
- Parametres SEO pour toutes les pages
- Gestion des utilisateurs

## Modeles de Base de Donnees

| Modele | Description |
|--------|-------------|
| `User` | Utilisateurs avec authentification et roles admin |
| `CategoryDB` | Categories de produits |
| `ProductDB` | Produits avec images, descriptions, dimensions |
| `Service` | Services proposes par Capsule |
| `PartnershipType` | Types de partenariats B2B |
| `ProcessStep` | Etapes du processus de travail |
| `FAQ` | Questions frequentes |
| `Testimonial` | Temoignages clients |
| `PageContent` | Contenu dynamique des pages |
| `SiteSettings` | Parametres generaux du site |
| `SEOSettings` | Parametres SEO par page |
| `HomepageStats` | Statistiques affichees sur la homepage |
| `HeroSection` | Configuration de la section hero |
| `ContactInfo` | Informations de contact et reseaux sociaux |

## Fonctionnalites

### Gestion des Reseaux Sociaux

Les reseaux sociaux suivants peuvent etre configures dans l'admin (`/admin/settings`):

| Reseau | Champ | Format |
|--------|-------|--------|
| **WhatsApp** | `whatsapp` | Numero de telephone (+33 7 XX XX XX XX) |
| **Facebook** | `facebook` | URL complete (https://facebook.com/...) |
| **Instagram** | `instagram` | URL complete (https://instagram.com/...) |
| **TikTok** | `tiktok` | URL complete (https://tiktok.com/@...) |
| **LinkedIn** | `linkedin` | URL complete (https://linkedin.com/company/...) |
| **Twitter / X** | `twitter` | URL complete (https://twitter.com/...) |
| **YouTube** | `youtube` | URL complete (https://youtube.com/...) |
| **Pinterest** | `pinterest` | URL complete (https://pinterest.com/...) |

Les icones des reseaux sociaux s'affichent automatiquement dans le footer du site lorsque les liens sont configures.

### SEO
Chaque page dispose de parametres SEO configurables:
- Meta title
- Meta description
- Meta keywords
- Open Graph (titre, description, image)
- Twitter Cards

### Gestion des Images
- Upload et traitement automatique des images
- Recadrage optionnel
- Optimisation pour le web
- Support des formats: PNG, JPG, JPEG, GIF, WebP, SVG

## Stack Technique

- **Backend**: Python Flask avec Blueprints
- **Base de donnees**: PostgreSQL avec SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Templating**: Jinja2
- **Serveur**: Gunicorn
- **Authentification**: Flask-Login
- **Traitement d'images**: Pillow
- **Architecture**: MVC avec services

## Design

### Palette de Couleurs
- Primaire: `#b8824e` (beige dore)
- Terre cuite: `#c86640`
- Cuivre: `#b87333`
- Or: `#d4af37`
- Arriere-plan: `#faf7f2`, `#f5ede1`

### Typographie
- Titres: Georgia (serif)
- Corps: System fonts (sans-serif)

## Administration

### Acces Admin
Pour acceder au panel d'administration:
1. Connectez-vous avec un compte admin sur `/auth/login`
2. Accedez a `/admin` pour le dashboard

Le premier utilisateur inscrit devient automatiquement administrateur.

### Configuration des Reseaux Sociaux
1. Allez dans Administration > Parametres
2. Remplissez les champs des reseaux sociaux souhaites
3. Cliquez sur "Enregistrer"

Les icones apparaitront automatiquement dans le footer du site.

## Contact

- Email: contact@capsule-maroc.com
- Telephone: +212 XX XX XX XX

---

2025 Capsule - Tous droits reserves
