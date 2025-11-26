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

### Variables Obligatoires (Secrets)

| Variable | Description |
|----------|-------------|
| `DATABASE_URL` | URL de connexion PostgreSQL |
| `SESSION_SECRET` | Cle secrete pour les sessions Flask |

### Variables pour la Creation d'Admin (Secrets)

| Variable | Description |
|----------|-------------|
| `ADMIN_USERNAME` | Nom d'utilisateur admin |
| `ADMIN_PASSWORD` | Mot de passe admin |
| `ADMIN_EMAIL` | Email admin |

### Variables Optionnelles (Contact & Reseaux Sociaux)

| Variable | Description |
|----------|-------------|
| `CONTACT_EMAIL` | Email de contact |
| `CONTACT_PHONE` | Numero de telephone |
| `CONTACT_WHATSAPP` | Numero WhatsApp |
| `CONTACT_ADDRESS` | Adresse |
| `SOCIAL_INSTAGRAM` | URL Instagram |
| `SOCIAL_FACEBOOK` | URL Facebook |
| `SOCIAL_TIKTOK` | URL TikTok |

## Installation et Lancement

### En Developpement

```bash
# 1. Configurer les variables d'environnement dans Replit Secrets
# DATABASE_URL, SESSION_SECRET, ADMIN_USERNAME, ADMIN_PASSWORD, ADMIN_EMAIL

# 2. Initialiser la base de donnees
python init_db.py --seed

# 3. Lancer l'application
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

### Script d'Initialisation

```bash
# Creer uniquement les tables
python init_db.py

# Creer les tables ET ajouter les donnees par defaut
python init_db.py --seed
```

## Structure du Projet

```
capsule/
├── app.py                  # Application Flask principale
├── main.py                 # Point d'entree gunicorn
├── init_db.py              # Script d'initialisation de la BDD
├── routes/                 # Blueprints Flask
│   ├── main.py            # Routes principales
│   ├── catalogue.py       # Routes catalogue
│   ├── business.py        # Routes B2B
│   ├── admin.py           # Panel d'administration
│   └── auth.py            # Authentification
├── models/                 # Modeles SQLAlchemy
├── services/               # Logique metier
├── utils/                  # Utilitaires
├── templates/              # Templates HTML (Jinja2)
└── static/                 # CSS, JS, Images
```

## Pages Disponibles

### Pages Principales
- **Accueil** (`/`) - Presentation et chiffres cles
- **Catalogue** (`/catalogue`) - Liste des produits
- **A Propos** (`/a-propos`) - Mission et valeurs
- **Contact** (`/contact`) - Formulaire de contact

### Pages Business (B2B)
- **Services** (`/services`) - Services de sourcing
- **Partenariats** (`/partenariats`) - Devenir partenaire
- **Notre Processus** (`/processus`) - Methodologie
- **FAQ** (`/faq`) - Questions frequentes

### Panel d'Administration (`/admin`)
- Dashboard avec statistiques
- Gestion des produits et categories
- Gestion des services et FAQ
- Configuration du site (contact, reseaux sociaux)
- Parametres SEO par page

## Reseaux Sociaux Supportes

Les reseaux suivants peuvent etre configures dans l'admin:
- **WhatsApp** - Numero pour les contacts directs
- **Facebook** - Page Facebook
- **Instagram** - Profil Instagram
- **TikTok** - Compte TikTok

## Stack Technique

- **Backend**: Python Flask avec Blueprints
- **Base de donnees**: PostgreSQL avec SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript
- **Templating**: Jinja2
- **Serveur**: Gunicorn
- **Authentification**: Flask-Login

## Design

### Palette de Couleurs
- Primaire: `#8B7355` (marron dore)
- Accent: `#b8824e` (beige dore)
- Backgrounds: `#faf7f2`, `#f5ede1`

---

2025 Capsule - Tous droits reserves

[English Version](README_EN.md)
