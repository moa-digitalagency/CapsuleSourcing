# Capsule - Site Web Vitrine

## Vue d'ensemble
Capsule est un site web vitrine dédié au sourcing de produits artisanaux marocains authentiques. Le site met en valeur le savoir-faire traditionnel marocain à travers une sélection de produits artisanaux de qualité.

## Architecture du Projet

### Stack Technique
- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript vanilla (pas de Node.js)
- **Templating**: Jinja2
- **Stockage**: Données en mémoire (products.py)

### Structure des Fichiers
```
.
├── app.py                  # Application Flask principale
├── products.py             # Base de données produits
├── templates/              # Templates HTML
│   ├── base.html          # Template de base
│   ├── index.html         # Page d'accueil
│   ├── catalogue.html     # Page catalogue
│   ├── product.html       # Page produit détaillée
│   ├── about.html         # Page à propos
│   └── contact.html       # Page contact
├── static/
│   ├── css/
│   │   └── style.css      # Styles CSS
│   ├── js/
│   │   └── script.js      # Scripts JavaScript
│   └── images/            # Images (actuellement placeholders)
└── attached_assets/        # Assets fournis par l'utilisateur
```

## Fonctionnalités

### Pages Principales
1. **Accueil** (`/`)
   - Hero section avec présentation de l'artisanat marocain
   - Produits phares
   - Valeurs de l'entreprise
   - Call-to-action

2. **Catalogue** (`/catalogue`)
   - Filtres par catégorie (Laiton, Céramique, Textile, Mobilier, Luminaires, Bijoux, Décoration)
   - Grille de produits responsive
   - Navigation par catégories

3. **Produit** (`/produit/<id>`)
   - Détails complets du produit
   - Caractéristiques techniques
   - Produits similaires
   - Bouton de demande de devis

4. **À Propos** (`/a-propos`)
   - Mission et valeurs de Capsule
   - Expertise en sourcing
   - Engagement qualité et commerce équitable

5. **Contact** (`/contact`)
   - Formulaire de contact
   - Informations de contact
   - Horaires d'ouverture

### Catégories de Produits
- **Laiton**: Ex-votos, mobiles, plateaux, patères, soliflores, bougeoirs
- **Céramique & Poterie**: Poteries terre cuite, vaisselle artisanale
- **Textile & Tissage**: Tapis, poufs, coussins, paniers
- **Mobilier**: Meubles en bois et tissages
- **Luminaires**: Appliques murales en laiton
- **Bijoux**: Bracelets Maaÿaz (sfifa traditionnelle)
- **Décoration**: Miroirs, cadres, trophées

## Design

### Palette de Couleurs
- **Primaire**: #b8824e (beige doré)
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

## Développement

### Lancer l'application
```bash
python app.py
```
L'application démarre sur `http://0.0.0.0:5000`

### Ajouter des Produits
Modifier le fichier `products.py` et ajouter des entrées au tableau `PRODUCTS`.

### Ajouter des Images
Placer les images dans `static/images/` et mettre à jour les chemins dans `products.py`.

## Modifications Récentes
- 25/11/2024: Refonte complète du design
  - Nouveau design moderne avec vraies images (images de stock)
  - Hero section avec grid layout et overlays sur images
  - Section testimonials clients avec avatars
  - Section newsletter pour demander le catalogue
  - Retrait de tous les prix (site catalogue, pas e-commerce)
  - Boutons "Demander Plus d'Informations" au lieu de prix
  - Images réelles sur tous les produits du catalogue
  - Design responsive amélioré
  - Overlays au hover sur les cartes produits

- 25/11/2024: Création initiale du projet
  - Structure Flask complète
  - 18 produits artisanaux marocains
  - 8 catégories de produits
  - Design inspiré de l'artisanat marocain
  - Pages responsive et modernes
  - Formulaire de contact fonctionnel

## Améliorations Futures
1. Ajouter de vraies images produits
2. Intégrer une base de données PostgreSQL
3. Ajouter un système d'administration
4. Implémenter la recherche de produits
5. Ajouter une galerie Instagram
6. Intégrer une newsletter
7. Optimiser le SEO
