#!/usr/bin/env python3
"""
Database Initialization Script for Capsule

This script initializes the database with all required tables and
seeds default data including all page content.
"""
import os
import sys
import logging
from flask import has_app_context

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def seed_page_content():
    """Seed all page content into database."""
    from app import app, db
    from models.database import PageContent
    
    def run_seed():
        def init_content(page, section, key, value):
            if not PageContent.query.filter_by(page=page, section=section, key=key).first():
                content = PageContent(page=page, section=section, key=key, value=value)
                db.session.add(content)
        
        init_content('index', 'featured', 'section_label', 'Notre Selection')
        init_content('index', 'featured', 'title', 'Nos Creations Phares')
        init_content('index', 'featured', 'description', "Une selection rigoureuse de pieces emblematiques representant le meilleur de l'artisanat marocain. Chaque creation est le fruit d'un savoir-faire ancestral transmis de generation en generation.")
        init_content('index', 'featured', 'showcase_category', 'Ceramique et Poterie')
        init_content('index', 'featured', 'showcase_title', 'Poterie Traditionnelle')
        init_content('index', 'featured', 'showcase_description', "Pieces uniques faconnees selon les techniques ancestrales de Fes et Safi. Chaque creation porte l'empreinte du maitre artisan qui l'a realisee.")
        init_content('index', 'featured', 'showcase_button', 'Decouvrir la Collection')
        init_content('index', 'featured', 'showcase_image', '/static/images/moroccan_artisan_han_11a3ad05.jpg')
        init_content('index', 'featured', 'cta_button', 'Voir Toute la Collection')
        
        init_content('index', 'stats', 'artisans_label', 'Artisans Partenaires')
        init_content('index', 'stats', 'products_label', 'References Produits')
        init_content('index', 'stats', 'partners_label', 'Clients B2B')
        init_content('index', 'stats', 'countries_label', 'Pays Livres')
        
        init_content('index', 'our_values', 'section_label', 'Nos Valeurs')
        init_content('index', 'our_values', 'title', 'Authenticite, Ethique, Excellence')
        init_content('index', 'our_values', 'description', "Trois piliers fondamentaux qui guident notre approche du sourcing artisanal et notre relation avec les artisans marocains.")
        
        init_content('index', 'our_values', 'value1_title', 'Authenticite')
        init_content('index', 'our_values', 'value1_description', "Chaque piece est creee a la main par des artisans marocains qualifies, perpetuant des traditions seculaires transmises de generation en generation.")
        init_content('index', 'our_values', 'value1_points', "Tracabilite complete de chaque produit|Techniques traditionnelles preservees|Materiaux locaux de qualite|Certification d'origine artisanale")
        
        init_content('index', 'our_values', 'value2_title', 'Ethique')
        init_content('index', 'our_values', 'value2_description', "Nous collaborons directement avec les artisans locaux pour garantir des pratiques equitables et soutenir les communautes creatrices.")
        init_content('index', 'our_values', 'value2_points', "Commerce equitable garanti|Remuneration juste des artisans|Soutien aux cooperatives locales|Respect des conditions de travail")
        
        init_content('index', 'our_values', 'value3_title', 'Excellence')
        init_content('index', 'our_values', 'value3_description', "Une selection rigoureuse de creations uniques alliant esthetique contemporaine et savoir-faire traditionnel d'exception.")
        init_content('index', 'our_values', 'value3_points', "Controle qualite systematique|Selection des meilleurs artisans|Finitions irreprochables|Standards internationaux")
        
        init_content('index', 'process', 'section_label', 'Notre Methode')
        init_content('index', 'process', 'title', 'Un Processus Eprouve')
        init_content('index', 'process', 'description', "De la selection a la livraison, nous assurons un accompagnement complet pour garantir votre satisfaction.")
        init_content('index', 'process', 'cta_button', 'Decouvrir Notre Processus')
        
        init_content('index', 'testimonials', 'section_label', 'Temoignages')
        init_content('index', 'testimonials', 'title', 'Ce Que Disent Nos Clients')
        
        init_content('index', 'cta', 'title', "Pret a Integrer l'Artisanat Marocain dans Vos Projets ?")
        init_content('index', 'cta', 'description', "Contactez notre equipe pour discuter de vos besoins et recevoir une proposition personnalisee.")
        init_content('index', 'cta', 'button1_text', 'Nous Contacter')
        init_content('index', 'cta', 'button2_text', 'Voir le Catalogue')
        
        init_content('index', 'newsletter', 'title', 'Restez Informes')
        init_content('index', 'newsletter', 'description', "Recevez en avant-premiere nos nouvelles collections et actualites du monde de l'artisanat marocain")
        init_content('index', 'newsletter', 'placeholder', 'Votre adresse email professionnelle')
        init_content('index', 'newsletter', 'button', "S'inscrire")
        
        init_content('about', 'header', 'title', 'Notre Histoire')
        init_content('about', 'header', 'subtitle', "Valoriser l'artisanat marocain d'exception")
        
        init_content('about', 'intro', 'title', 'Quand la Tradition Rencontre la Modernite')
        init_content('about', 'intro', 'description', "Capsule est nee d'une passion profonde pour l'artisanat marocain et du desir de faire rayonner la richesse du savoir-faire ancestral a travers le monde.")
        
        init_content('about', 'mission', 'title', 'Notre Mission')
        init_content('about', 'mission', 'description', "Sourcer et promouvoir des creations artisanales marocaines authentiques, en collaboration directe avec les artisans. Nous preservons les techniques ancestrales tout en les adaptant aux sensibilites contemporaines.")
        
        init_content('about', 'our_values', 'title', 'Nos Valeurs')
        init_content('about', 'our_values', 'description', "Authenticite, excellence et commerce equitable guident chacune de nos actions. Nous croyons en des relations transparentes avec les artisans, garantissant une remuneration juste et des conditions dignes.")
        
        init_content('about', 'expertise', 'title', 'Notre Expertise')
        init_content('about', 'expertise', 'description', "Forte d'une connaissance approfondie du terrain artisanal marocain, notre equipe selectionne rigoureusement chaque piece pour sa qualite, son authenticite et son caractere unique.")
        
        init_content('about', 'sourcing', 'title', "L'Art du Sourcing")
        init_content('about', 'sourcing', 'description', "Chaque creation de notre collection a ete soigneusement choisie lors de nos explorations a travers le Maroc. Des souks de Marrakech aux ateliers de Fes, en passant par les villages berberes, nous parcourons le pays a la recherche des artisans les plus talentueux.")
        init_content('about', 'sourcing', 'intro', "Nous valorisons particulierement les techniques traditionnelles :")
        init_content('about', 'sourcing', 'techniques', "Le travail du laiton - Ciselage, martelage et gravure selon des methodes ancestrales|La ceramique - Poterie tournee a la main et emaillee avec des pigments naturels|Le tissage - Tapis berberes, coussins brodes et textiles sur metiers traditionnels|La maroquinerie - Cuir tanne naturellement et travaille a la main|La bijouterie artisanale - Bracelets Maayaz tisses selon la methode de la sfifa")
        
        init_content('about', 'commitments', 'title', 'Nos Engagements')
        init_content('about', 'commitments', 'item1_title', 'Qualite Garantie')
        init_content('about', 'commitments', 'item1_description', "Chaque piece est inspectee pour assurer une qualite artisanale irreprochable.")
        init_content('about', 'commitments', 'item2_title', 'Commerce Equitable')
        init_content('about', 'commitments', 'item2_description', "Remuneration juste des artisans et partenariats durables.")
        init_content('about', 'commitments', 'item3_title', '100% Authentique')
        init_content('about', 'commitments', 'item3_description', "Produits entierement artisanaux, fabriques selon des techniques traditionnelles.")
        init_content('about', 'commitments', 'item4_title', 'Durabilite')
        init_content('about', 'commitments', 'item4_description', "Preservation des savoir-faire ancestraux et pratiques responsables.")
        
        init_content('about', 'cta', 'title', 'Collaborons Ensemble')
        init_content('about', 'cta', 'description', "Professionnel souhaitant enrichir votre offre avec nos creations artisanales ? Contactez-nous pour echanger sur vos besoins.")
        init_content('about', 'cta', 'button', 'Nous Contacter')
        
        init_content('services', 'header', 'title', 'Nos Services')
        init_content('services', 'header', 'subtitle', "Un accompagnement complet pour integrer l'artisanat marocain dans vos projets")
        
        init_content('services', 'intro', 'title', 'Votre Partenaire Sourcing')
        init_content('services', 'intro', 'description', "Capsule vous accompagne a chaque etape de votre projet, de la selection des produits a la livraison finale. Notre expertise du terrain marocain et notre reseau d'artisans qualifies vous garantissent des produits authentiques et de qualite.")
        
        init_content('services', 'features', 'feature1_title', 'Reactivite')
        init_content('services', 'features', 'feature1_description', "Reponse sous 24h a toutes vos demandes et devis personnalises sous 48h.")
        init_content('services', 'features', 'feature2_title', 'Transparence')
        init_content('services', 'features', 'feature2_description', "Suivi en temps reel de votre commande et communication directe avec notre equipe.")
        init_content('services', 'features', 'feature3_title', 'Flexibilite')
        init_content('services', 'features', 'feature3_description', "Adaptation a vos contraintes de volume, delais et specifications techniques.")
        init_content('services', 'features', 'feature4_title', 'Garantie')
        init_content('services', 'features', 'feature4_description', "Remplacement ou remboursement en cas de non-conformite a votre commande.")
        
        init_content('services', 'cta', 'title', 'Pret a Demarrer Votre Projet ?')
        init_content('services', 'cta', 'description', "Contactez-nous pour discuter de vos besoins et recevoir une proposition sur mesure.")
        init_content('services', 'cta', 'button', 'Nous Contacter')
        
        init_content('contact', 'header', 'title', 'Contactez-Nous')
        init_content('contact', 'header', 'subtitle', "Une question ? Un projet ? Nous sommes a votre ecoute")
        
        init_content('contact', 'form', 'title', 'Parlons de Votre Projet')
        init_content('contact', 'form', 'description', "Que vous soyez professionnel a la recherche de pieces artisanales pour votre boutique, architecte d'interieur, ou simplement passionne par l'artisanat, nous serons ravis d'echanger avec vous.")
        init_content('contact', 'form', 'name_label', 'Nom complet')
        init_content('contact', 'form', 'name_placeholder', 'Votre nom')
        init_content('contact', 'form', 'email_label', 'Email')
        init_content('contact', 'form', 'email_placeholder', 'votre@email.com')
        init_content('contact', 'form', 'company_label', 'Entreprise (optionnel)')
        init_content('contact', 'form', 'company_placeholder', 'Nom de votre entreprise')
        init_content('contact', 'form', 'message_label', 'Votre message')
        init_content('contact', 'form', 'message_placeholder', 'Comment pouvons-nous vous aider ?')
        init_content('contact', 'form', 'submit_button', 'Envoyer via WhatsApp')
        
        init_content('contact', 'info', 'social_title', 'Suivez-nous')
        init_content('contact', 'info', 'hours_title', "Horaires d'ouverture")
        init_content('contact', 'info', 'hours_line1', 'Lundi - Vendredi : 9h - 18h')
        init_content('contact', 'info', 'hours_line2', 'Samedi : 10h - 16h')
        
        init_content('catalogue', 'header', 'title', 'Notre Collection')
        init_content('catalogue', 'header', 'subtitle', "Decouvrez notre selection de produits artisanaux marocains")
        init_content('catalogue', 'filter', 'all_categories', 'Toutes les categories')
        init_content('catalogue', 'empty', 'message', 'Aucun produit trouve dans cette categorie.')
        
        init_content('faq', 'header', 'title', 'Questions Frequentes')
        init_content('faq', 'header', 'subtitle', "Retrouvez les reponses aux questions les plus posees")
        init_content('faq', 'cta', 'title', "Vous n'avez pas trouve votre reponse ?")
        init_content('faq', 'cta', 'description', "Notre equipe est disponible pour repondre a toutes vos questions.")
        init_content('faq', 'cta', 'button', 'Nous Contacter')
        
        init_content('partenariats', 'header', 'title', 'Partenariats')
        init_content('partenariats', 'header', 'subtitle', "Des solutions adaptees a chaque type de partenaire")
        init_content('partenariats', 'intro', 'title', 'Devenez Partenaire')
        init_content('partenariats', 'intro', 'description', "Nous collaborons avec des professionnels de tous horizons partageant notre passion pour l'artisanat authentique.")
        init_content('partenariats', 'cta', 'title', 'Interesse par un Partenariat ?')
        init_content('partenariats', 'cta', 'description', "Discutons ensemble de la meilleure formule pour votre activite.")
        init_content('partenariats', 'cta', 'button', 'Nous Contacter')
        
        init_content('processus', 'header', 'title', 'Notre Processus')
        init_content('processus', 'header', 'subtitle', "Une methodologie eprouvee pour des projets reussis")
        init_content('processus', 'intro', 'title', 'De la Commande a la Livraison')
        init_content('processus', 'intro', 'description', "Nous avons developpe un processus structure pour garantir la qualite et le respect des delais a chaque etape de votre projet.")
        init_content('processus', 'cta', 'title', 'Pret a Lancer Votre Projet ?')
        init_content('processus', 'cta', 'description', "Contactez-nous pour discuter de vos besoins et demarrer notre collaboration.")
        init_content('processus', 'cta', 'button', 'Demarrer un Projet')
        
        init_content('global', 'nav', 'home', 'Accueil')
        init_content('global', 'nav', 'enterprise', 'Entreprise')
        init_content('global', 'nav', 'catalogue', 'Catalogue')
        init_content('global', 'nav', 'services', 'Services')
        init_content('global', 'nav', 'faq', 'FAQ')
        init_content('global', 'nav', 'contact', 'Contact')
        init_content('global', 'nav', 'about', 'A Propos')
        init_content('global', 'nav', 'partnerships', 'Partenariats')
        init_content('global', 'nav', 'process', 'Processus')
        
        init_content('global', 'footer', 'tagline', "L'excellence de l'artisanat marocain a portee de main")
        init_content('global', 'footer', 'navigation_title', 'Navigation')
        init_content('global', 'footer', 'enterprise_title', 'Entreprise')
        init_content('global', 'footer', 'contact_title', 'Contact')
        init_content('global', 'footer', 'copyright', '2024 Capsule. Tous droits reserves.')
        
        db.session.commit()
        logger.info("Created all page content")
    
    if has_app_context():
        run_seed()
    else:
        with app.app_context():
            run_seed()


def seed_all_data():
    """Seed the database with all default data from templates."""
    from app import app, db
    from models.database import (
        User, ContactInfo, HeroSection, HomepageStats, 
        SEOSettings, CategoryDB, ProductDB, Service, 
        PartnershipType, ProcessStep, FAQ, Testimonial
    )
    
    def run_seed():
        logger.info("Seeding all default data...")
        
        if not ContactInfo.query.first():
            contact = ContactInfo(
                email="contact@capsule-maroc.com",
                phone="+212 XX XX XX XX",
                whatsapp="+33774496440",
                address="Marrakech, Maroc",
                instagram="https://instagram.com/capsule.maroc",
                facebook="https://facebook.com/capsule.maroc",
                tiktok="https://tiktok.com/@capsule.maroc"
            )
            db.session.add(contact)
            logger.info("Created contact info")
        
        if not HeroSection.query.first():
            hero = HeroSection(
                title="L'Art du Savoir-Faire Marocain",
                subtitle="Des pieces uniques, faconnees par des mains expertes",
                button_text="Decouvrir la Collection",
                main_image="/static/images/moroccan_brass_craft_91c1b440.jpg",
                card1_title="Ebenisterie",
                card1_subtitle="Le travail du bois traditionnel",
                card1_image="/static/images/moroccan_brass_craft_59d29144.jpg",
                card1_link="mobilier",
                card2_title="Fibres Naturelles",
                card2_subtitle="Vannerie et tissage artisanal",
                card2_image="/static/images/moroccan_brass_craft_5197c08b.jpg",
                card2_link="textile"
            )
            db.session.add(hero)
            logger.info("Created hero section")
        
        if not HomepageStats.query.first():
            stats = HomepageStats(
                artisans=50,
                products=200,
                partners=35,
                countries=12
            )
            db.session.add(stats)
            logger.info("Created homepage stats")
        
        default_categories = [
            {'id': 'mobilier', 'name': 'Mobilier', 'icon': 'home', 'order': 1},
            {'id': 'textile', 'name': 'Textile', 'icon': 'layers', 'order': 2},
            {'id': 'ceramique', 'name': 'Ceramique', 'icon': 'coffee', 'order': 3},
            {'id': 'cuir', 'name': 'Cuir', 'icon': 'briefcase', 'order': 4},
            {'id': 'metal', 'name': 'Metal', 'icon': 'tool', 'order': 5},
            {'id': 'bois', 'name': 'Bois', 'icon': 'box', 'order': 6},
        ]
        
        for cat in default_categories:
            existing = db.session.get(CategoryDB, cat['id'])
            if not existing:
                category = CategoryDB(**cat)
                db.session.add(category)
        logger.info("Created categories")
        
        if Service.query.count() == 0:
            services = [
                Service(
                    title="Sourcing Sur Mesure",
                    description="Identification et selection de produits artisanaux selon vos specifications. Nous parcourons le Maroc pour trouver les pieces qui correspondent exactement a vos besoins.",
                    icon="search",
                    order=1
                ),
                Service(
                    title="Controle Qualite",
                    description="Inspection rigoureuse de chaque piece avant expedition. Notre equipe verifie la conformite aux standards definis et garantit une qualite irreprochable.",
                    icon="check",
                    order=2
                ),
                Service(
                    title="Logistique Export",
                    description="Gestion complete de l'expedition internationale, de l'emballage a la livraison. Nous assurons le transport securise de vos commandes partout dans le monde.",
                    icon="truck",
                    order=3
                ),
                Service(
                    title="Accompagnement Projet",
                    description="Conseil et suivi personnalise pour vos projets d'amenagement ou de decoration. Un interlocuteur dedie vous accompagne de la conception a la realisation.",
                    icon="users",
                    order=4
                )
            ]
            for service in services:
                db.session.add(service)
            logger.info("Created services")
        
        if PartnershipType.query.count() == 0:
            partnerships = [
                PartnershipType(
                    title="Distributeur",
                    description="Integrez notre collection dans votre offre commerciale et proposez a vos clients des pieces artisanales authentiques.",
                    benefits="Tarifs preferentiels sur catalogue|Exclusivite territoriale possible|Support marketing et visuels|Formation produit",
                    order=1
                ),
                PartnershipType(
                    title="Hotellerie & Restauration",
                    description="Creez une ambiance unique dans vos etablissements avec des pieces sur mesure refletant l'art de vivre marocain.",
                    benefits="Projets sur mesure|Accompagnement decoration|Delais adaptes aux chantiers|Remplacement et SAV dedies",
                    order=2
                ),
                PartnershipType(
                    title="Architectes & Decorateurs",
                    description="Enrichissez vos projets avec des pieces artisanales uniques selectionnees pour leur qualite et leur authenticite.",
                    benefits="Acces collection complete|Echantillons disponibles|Commandes speciales|Livraison sur chantier",
                    order=3
                )
            ]
            for partnership in partnerships:
                db.session.add(partnership)
            logger.info("Created partnership types")
        
        if ProcessStep.query.count() == 0:
            steps = [
                ProcessStep(
                    number="01",
                    title="Decouverte",
                    description="Analyse de vos besoins et definition du cahier des charges. Nous echangeons sur vos attentes, contraintes et objectifs pour cerner parfaitement votre projet.",
                    order=1
                ),
                ProcessStep(
                    number="02",
                    title="Selection",
                    description="Identification des artisans et produits correspondant a vos criteres. Notre reseau nous permet de trouver les meilleures pieces pour votre projet.",
                    order=2
                ),
                ProcessStep(
                    number="03",
                    title="Production",
                    description="Fabrication artisanale avec suivi qualite rigoureux. Chaque etape est documentee et validee pour garantir la conformite.",
                    order=3
                ),
                ProcessStep(
                    number="04",
                    title="Livraison",
                    description="Expedition soignee et livraison dans les delais. Emballage securise et transport adapte pour une reception en parfait etat.",
                    order=4
                )
            ]
            for step in steps:
                db.session.add(step)
            logger.info("Created process steps")
        
        if FAQ.query.count() == 0:
            faqs = [
                FAQ(
                    question="Quels types de produits proposez-vous ?",
                    answer="Nous proposons une large gamme de produits artisanaux marocains : ceramique et poterie, textiles (tapis, coussins), maroquinerie, travail du metal (laiton, fer forge), bois sculpte, vannerie et bien d'autres. Chaque piece est fabriquee a la main par des artisans qualifies.",
                    order=1
                ),
                FAQ(
                    question="Quels sont vos delais de livraison ?",
                    answer="Les delais varient selon le type de commande. Pour les produits en stock, comptez 2 a 4 semaines. Pour les commandes sur mesure ou en quantite, les delais sont de 6 a 12 semaines selon la complexite. Nous vous communiquons un planning precis lors de la validation de commande.",
                    order=2
                ),
                FAQ(
                    question="Quelle est la quantite minimum de commande ?",
                    answer="Nous travaillons principalement avec des professionnels (B2B). La quantite minimum depend des produits mais nous sommes flexibles et adaptons nos offres a vos besoins. Contactez-nous pour discuter de votre projet.",
                    order=3
                ),
                FAQ(
                    question="Livrez-vous a l'international ?",
                    answer="Oui, nous livrons dans le monde entier. Notre equipe logistique gere l'ensemble des formalites d'export et vous accompagne pour une livraison sans souci. Les frais de port sont calcules selon la destination et le volume.",
                    order=4
                ),
                FAQ(
                    question="Proposez-vous des produits personnalises ?",
                    answer="Absolument ! La personnalisation est l'une de nos forces. Nos artisans peuvent adapter les dimensions, couleurs, motifs selon vos specifications. Nous pouvons egalement creer des pieces uniques sur cahier des charges.",
                    order=5
                ),
                FAQ(
                    question="Comment garantissez-vous la qualite ?",
                    answer="Chaque piece est inspectee avant expedition selon des criteres stricts. Nous travaillons uniquement avec des artisans selectionnes pour leur savoir-faire. En cas de non-conformite, nous assurons le remplacement ou le remboursement.",
                    order=6
                )
            ]
            for faq in faqs:
                db.session.add(faq)
            logger.info("Created FAQs")
        
        if Testimonial.query.count() == 0:
            testimonials = [
                Testimonial(
                    text="La qualite des produits Capsule est exceptionnelle. Chaque piece raconte une histoire et reflete un savoir-faire unique. Nos clients adorent l'authenticite de ces creations.",
                    author_name="Sarah Chen",
                    author_title="Boutique Le Souk, Paris",
                    author_image="/static/images/avatar1.jpg",
                    order=1
                ),
                Testimonial(
                    text="Un partenariat formidable. Capsule nous permet d'offrir a nos clients des pieces artisanales authentiques avec une tracabilite complete. Le service est impeccable.",
                    author_name="Marc Dubois",
                    author_title="Architecte d'interieur",
                    author_image="/static/images/avatar2.jpg",
                    order=2
                ),
                Testimonial(
                    text="Excellente reactivite et produits conformes a nos attentes. Capsule comprend parfaitement les exigences du secteur hotelier haut de gamme.",
                    author_name="Julie Martin",
                    author_title="Directrice Achats, Groupe Hotelier",
                    author_image="/static/images/avatar1.jpg",
                    order=3
                )
            ]
            for testimonial in testimonials:
                db.session.add(testimonial)
            logger.info("Created testimonials")
        
        if ProductDB.query.count() == 0:
            products = [
                ProductDB(
                    name="Vase en Ceramique de Fes",
                    category_id="ceramique",
                    description="Magnifique vase en ceramique traditionnelle de Fes, orne de motifs geometriques bleus caracteristiques de l'artisanat fassi.",
                    details="Ce vase est realise selon les techniques ancestrales des potiers de Fes. Chaque piece est unique, faconnee a la main et decoree avec des pigments naturels.",
                    dimensions="H: 35cm, D: 20cm",
                    material="Ceramique emaillee",
                    image="/static/images/moroccan_artisan_han_11a3ad05.jpg",
                    is_featured=True,
                    order=1
                ),
                ProductDB(
                    name="Lanterne en Laiton Cisele",
                    category_id="metal",
                    description="Lanterne traditionnelle en laiton finement cisele, creant de magnifiques jeux de lumiere.",
                    details="Travail artisanal realise par les maitres ciseleurs de Marrakech. Le laiton est martele et perce a la main pour creer des motifs d'une grande finesse.",
                    dimensions="H: 45cm, L: 25cm",
                    material="Laiton",
                    image="/static/images/moroccan_brass_craft_8cacf1dc.jpg",
                    is_featured=True,
                    order=2
                ),
                ProductDB(
                    name="Tapis Berbere Authentique",
                    category_id="textile",
                    description="Tapis berbere tisse a la main dans l'Atlas, avec des motifs traditionnels et des couleurs naturelles.",
                    details="Chaque tapis est une piece unique, tissee par des artisanes berberes selon des techniques transmises de generation en generation.",
                    dimensions="200cm x 150cm",
                    material="Laine naturelle",
                    image="/static/images/moroccan_artisan_han_2e2686eb.jpg",
                    is_featured=True,
                    order=3
                ),
                ProductDB(
                    name="Table Basse en Thuya",
                    category_id="bois",
                    description="Table basse en bois de thuya sculpte, avec des incrustations de nacre et de citronnier.",
                    details="Le thuya est un bois precieux de la region d'Essaouira, reconnu pour ses veines uniques et son parfum delicat.",
                    dimensions="H: 40cm, L: 80cm, P: 50cm",
                    material="Bois de thuya, nacre, citronnier",
                    image="/static/images/moroccan_brass_craft_af2c930a.jpg",
                    is_featured=True,
                    order=4
                ),
                ProductDB(
                    name="Pouf en Cuir Tanne",
                    category_id="cuir",
                    description="Pouf traditionnel en cuir tanne naturellement, brode avec des fils de soie.",
                    details="Le cuir est tanne selon la methode traditionnelle des tanneries de Fes, sans produits chimiques.",
                    dimensions="D: 50cm, H: 35cm",
                    material="Cuir de chevre",
                    image="/static/images/moroccan_artisan_han_43aa89bc.jpg",
                    is_featured=False,
                    order=5
                ),
                ProductDB(
                    name="Panier en Osier Tresse",
                    category_id="mobilier",
                    description="Panier artisanal en osier tresse, ideal pour le rangement ou la decoration.",
                    details="Fabrique par les vanniers du Rif, chaque panier est tresse a la main avec des fibres naturelles.",
                    dimensions="H: 30cm, D: 35cm",
                    material="Osier naturel",
                    image="/static/images/moroccan_brass_craft_5cbdcb61.jpg",
                    is_featured=False,
                    order=6
                ),
                ProductDB(
                    name="Miroir en Laiton Martele",
                    category_id="metal",
                    description="Miroir decoratif encadre de laiton finement martele, parfait pour sublimer votre interieur.",
                    details="Travail traditionnel des artisans de Marrakech, le cadre en laiton est martele a la main pour creer des reflets uniques.",
                    dimensions="D: 60cm",
                    material="Laiton, miroir",
                    image="/static/images/moroccan_brass_craft_5197c08b.jpg",
                    is_featured=True,
                    order=7
                ),
                ProductDB(
                    name="Tajine Decoratif Peint",
                    category_id="ceramique",
                    description="Tajine decoratif peint a la main avec des motifs traditionnels fassis.",
                    details="Cette piece decorative est realisee par les maitres potiers de Fes. Les couleurs sont obtenues a partir de pigments naturels.",
                    dimensions="D: 30cm, H: 25cm",
                    material="Terre cuite emaillee",
                    image="/static/images/moroccan_pottery_cer_26051764.jpg",
                    is_featured=False,
                    order=8
                ),
                ProductDB(
                    name="Coussin Brode Main",
                    category_id="textile",
                    description="Coussin brode a la main avec des motifs geometriques berberes traditionnels.",
                    details="Chaque coussin est une piece unique, brodee par des artisanes de l'Atlas selon des techniques ancestrales.",
                    dimensions="50cm x 50cm",
                    material="Coton, fils de soie",
                    image="/static/images/moroccan_artisan_wor_de89e55a.jpg",
                    is_featured=False,
                    order=9
                ),
                ProductDB(
                    name="Boite a Bijoux en Thuya",
                    category_id="bois",
                    description="Boite a bijoux en bois de thuya avec incrustations de nacre et citronnier.",
                    details="Le thuya d'Essaouira est un bois precieux aux veines uniques. Chaque boite est sculptee et polie a la main.",
                    dimensions="L: 15cm, l: 10cm, H: 8cm",
                    material="Bois de thuya, nacre",
                    image="/static/images/moroccan_woodwork_fu_74825e67.jpg",
                    is_featured=False,
                    order=10
                ),
                ProductDB(
                    name="Sac en Cuir Naturel",
                    category_id="cuir",
                    description="Sac a main en cuir tanne naturellement dans les tanneries de Fes.",
                    details="Le cuir est tanne selon la methode traditionnelle seculaire, sans produits chimiques, puis teint avec des colorants naturels.",
                    dimensions="L: 35cm, H: 25cm",
                    material="Cuir de chevre tanne",
                    image="/static/images/moroccan_artisan_han_43aa89bc.jpg",
                    is_featured=False,
                    order=11
                ),
                ProductDB(
                    name="Plateau en Laiton Grave",
                    category_id="metal",
                    description="Plateau decoratif en laiton grave avec des arabesques traditionnelles.",
                    details="Grave a la main par les maitres artisans de Fes, ce plateau allie beaute et fonctionnalite.",
                    dimensions="D: 50cm",
                    material="Laiton grave",
                    image="/static/images/moroccan_brass_metal_6cc61071.jpg",
                    is_featured=False,
                    order=12
                ),
                ProductDB(
                    name="Assiette Decorative Bleue",
                    category_id="ceramique",
                    description="Assiette decorative en ceramique bleue de Fes, ornee de motifs floraux.",
                    details="La ceramique bleue de Fes est reconnaissable a ses motifs bleus cobalt sur fond blanc, technique heritee des Andalous.",
                    dimensions="D: 35cm",
                    material="Ceramique emaillee",
                    image="/static/images/moroccan_pottery_cer_db1d11f8.jpg",
                    is_featured=False,
                    order=13
                ),
                ProductDB(
                    name="Tabouret en Bois Sculpte",
                    category_id="mobilier",
                    description="Tabouret traditionnel en bois sculpte a la main avec des motifs geometriques.",
                    details="Fabrique par les ebenistes d'Essaouira, ce tabouret allie fonctionnalite et art decoratif.",
                    dimensions="H: 45cm, D: 30cm",
                    material="Bois de cedre",
                    image="/static/images/moroccan_woodwork_fu_19c5df4f.jpg",
                    is_featured=False,
                    order=14
                ),
                ProductDB(
                    name="Bougeoir en Fer Forge",
                    category_id="metal",
                    description="Bougeoir en fer forge a la main, design contemporain inspire de l'artisanat marocain.",
                    details="Realise par les forgerons de Marrakech selon des techniques ancestrales adaptees au design moderne.",
                    dimensions="H: 35cm, D: 12cm",
                    material="Fer forge",
                    image="/static/images/moroccan_brass_craft_91c1b440.jpg",
                    is_featured=False,
                    order=15
                ),
                ProductDB(
                    name="Cheche en Coton",
                    category_id="textile",
                    description="Cheche traditionnel en coton leger, tisse a la main dans le sud marocain.",
                    details="Ce foulard polyvalent est tisse par les artisans du desert selon des techniques ancestrales touaregues.",
                    dimensions="200cm x 100cm",
                    material="Coton naturel",
                    image="/static/images/moroccan_artisan_han_2e2686eb.jpg",
                    is_featured=False,
                    order=16
                ),
                ProductDB(
                    name="Cadre Photo en Laiton",
                    category_id="metal",
                    description="Cadre photo decoratif en laiton martele avec des motifs floraux.",
                    details="Fabrique a la main par les artisans de Marrakech, ce cadre sublime vos photos preferees.",
                    dimensions="20cm x 25cm",
                    material="Laiton martele",
                    image="/static/images/moroccan_brass_craft_af2c930a.jpg",
                    is_featured=False,
                    order=17
                ),
                ProductDB(
                    name="Vide-Poche en Ceramique",
                    category_id="ceramique",
                    description="Petit vide-poche en ceramique peinte, ideal pour les cles ou bijoux.",
                    details="Piece decorative et fonctionnelle, peinte a la main avec des motifs traditionnels de Safi.",
                    dimensions="D: 15cm, H: 5cm",
                    material="Ceramique peinte",
                    image="/static/images/moroccan_artisan_han_11a3ad05.jpg",
                    is_featured=False,
                    order=18
                )
            ]
            for product in products:
                db.session.add(product)
            logger.info("Created sample products")
        
        pages = ['index', 'catalogue', 'about', 'contact', 'services', 'partenariats', 'processus', 'faq']
        seo_defaults = {
            'index': {'meta_title': 'Capsule - Artisanat Marocain d\'Exception', 'meta_description': 'Decouvrez notre selection de produits artisanaux marocains authentiques. Sourcing sur mesure pour professionnels.'},
            'catalogue': {'meta_title': 'Catalogue - Capsule', 'meta_description': 'Explorez notre collection de produits artisanaux marocains: ceramique, textile, cuir, metal et bois.'},
            'about': {'meta_title': 'Notre Histoire - Capsule', 'meta_description': 'Decouvrez l\'histoire de Capsule et notre engagement pour valoriser l\'artisanat marocain d\'exception.'},
            'contact': {'meta_title': 'Contact - Capsule', 'meta_description': 'Contactez-nous pour discuter de vos projets d\'artisanat marocain. Nous sommes a votre ecoute.'},
            'services': {'meta_title': 'Nos Services - Capsule', 'meta_description': 'Sourcing sur mesure, controle qualite, logistique export. Decouvrez nos services d\'accompagnement.'},
            'partenariats': {'meta_title': 'Partenariats - Capsule', 'meta_description': 'Devenez partenaire Capsule. Solutions pour distributeurs, hoteliers et architectes.'},
            'processus': {'meta_title': 'Notre Processus - Capsule', 'meta_description': 'De la commande a la livraison, decouvrez notre methodologie eprouvee.'},
            'faq': {'meta_title': 'FAQ - Capsule', 'meta_description': 'Questions frequentes sur nos services, delais, livraisons et produits artisanaux.'}
        }
        for page in pages:
            if not SEOSettings.query.filter_by(page=page).first():
                defaults = seo_defaults.get(page, {})
                seo = SEOSettings(
                    page=page,
                    meta_title=defaults.get('meta_title', f'{page.capitalize()} - Capsule'),
                    meta_description=defaults.get('meta_description', '')
                )
                db.session.add(seo)
        logger.info("Created SEO settings")
        
        db.session.commit()
        logger.info("All default data seeded successfully!")
        
        return True
    
    if has_app_context():
        return run_seed()
    else:
        with app.app_context():
            return run_seed()


def main():
    """Main entry point."""
    logger.info("=" * 50)
    logger.info("Capsule Database Initialization")
    logger.info("=" * 50)
    
    if not os.environ.get('DATABASE_URL'):
        logger.error("DATABASE_URL environment variable is not set!")
        sys.exit(1)
    
    try:
        from app import app, db
        
        with app.app_context():
            import models.database
            logger.info("Creating database tables...")
            db.create_all()
            logger.info("Database tables created successfully!")
        
        seed_all_data()
        seed_page_content()
    
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    
    logger.info("")
    logger.info("=" * 50)
    logger.info("Initialization complete!")
    logger.info("=" * 50)


if __name__ == '__main__':
    main()
