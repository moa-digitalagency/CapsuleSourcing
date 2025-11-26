# Capsule - Plateforme B2B de Sourcing Artisanat Marocain

Capsule est une plateforme B2B specialisee dans le sourcing de produits artisanaux marocains authentiques, destinee aux professionnels (hotels, decorateurs, boutiques).

## Presentation

L'Art du Savoir-Faire Marocain - Des pieces uniques, faconnees par des mains expertes.

### Notre Mission

Connecter les artisans marocains aux professionnels du monde entier en garantissant:
- **Authenticite** - Produits 100% artisanaux marocains
- **Ethique** - Commerce equitable et respect des artisans
- **Excellence** - Selection rigoureuse et controle qualite

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
├── routes/                 # Blueprints Flask
│   ├── main.py            # Routes principales (index, about, contact)
│   ├── catalogue.py       # Routes catalogue et produits
│   └── business.py        # Routes B2B (services, partenariats, faq)
├── models/                 # Modeles de donnees
│   └── product.py         # Classes Product et Category
├── services/               # Logique metier
│   └── product_service.py # Service de gestion des produits
├── templates/              # Templates HTML (Jinja2)
├── static/
│   ├── css/style.css      # Styles CSS
│   ├── js/script.js       # Scripts JavaScript
│   └── images/            # Images du site
└── README.md
```

## Pages Disponibles

### Pages Principales
- **Accueil** (`/`) - Presentation et chiffres cles
- **Catalogue** (`/catalogue`) - Liste des produits avec filtres
- **Produit** (`/produit/<id>`) - Details d'un produit
- **A Propos** (`/a-propos`) - Mission et valeurs
- **Contact** (`/contact`) - Formulaire de contact avec WhatsApp

### Pages Business (B2B)
- **Services** (`/services`) - Services de sourcing et personnalisation
- **Partenariats** (`/partenariats`) - Devenir partenaire
- **Notre Processus** (`/processus`) - Comment nous travaillons
- **FAQ** (`/faq`) - Questions frequentes

## Stack Technique

- **Backend**: Python Flask avec Blueprints
- **Frontend**: HTML5, CSS3, JavaScript vanilla
- **Templating**: Jinja2
- **Serveur**: Gunicorn
- **Architecture**: MVC avec services

## Installation et Lancement

```bash
# Installer les dependances
pip install flask flask-sqlalchemy gunicorn werkzeug email-validator psycopg2-binary

# Lancer l'application
gunicorn --bind 0.0.0.0:5000 --reuse-port --reload main:app
```

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

## Contact

- Email: contact@capsule-maroc.com
- Telephone: +212 XX XX XX XX

---

2025 Capsule - Tous droits reserves
