from flask import render_template
from routes import business_bp


@business_bp.route('/services')
def services():
    services_list = [
        {
            'title': 'Sourcing Sur Mesure',
            'description': 'Nous identifions et selectionnons les artisans et produits correspondant exactement a vos besoins.',
            'icon': 'search'
        },
        {
            'title': 'Controle Qualite',
            'description': 'Chaque piece est inspectee selon nos standards rigoureux avant expedition.',
            'icon': 'check'
        },
        {
            'title': 'Logistique Complete',
            'description': 'Gestion integrale du transport, des douanes et de la livraison a destination.',
            'icon': 'truck'
        },
        {
            'title': 'Accompagnement Projet',
            'description': 'Conseil personnalise pour integrer l\'artisanat marocain dans vos collections.',
            'icon': 'users'
        }
    ]
    return render_template('services.html', services=services_list)


@business_bp.route('/partenariats')
def partenariats():
    partnership_types = [
        {
            'title': 'Distributeurs & Retailers',
            'description': 'Approvisionnement regulier en produits artisanaux authentiques pour votre reseau de boutiques.',
            'benefits': ['Catalogues exclusifs', 'Prix preferentiels', 'Stock garanti', 'Support marketing']
        },
        {
            'title': 'Hotels & Hospitality',
            'description': 'Amenagement et decoration avec des pieces uniques pour creer une experience client memorable.',
            'benefits': ['Pieces sur mesure', 'Installation complete', 'Renouvellement saisonnier', 'Maintenance']
        },
        {
            'title': 'Architectes & Decorateurs',
            'description': 'Acces a notre reseau d\'artisans pour des projets de decoration d\'interieur uniques.',
            'benefits': ['Creations personnalisees', 'Echantillonnage', 'Suivi de production', 'Delais garantis']
        },
        {
            'title': 'Marques & Labels',
            'description': 'Co-creation de collections capsules alliant votre identite et le savoir-faire marocain.',
            'benefits': ['Design collaboratif', 'Exclusivite', 'Storytelling', 'Production ethique']
        }
    ]
    return render_template('partenariats.html', partnership_types=partnership_types)


@business_bp.route('/processus')
def processus():
    steps = [
        {
            'number': '01',
            'title': 'Decouverte',
            'description': 'Analyse de vos besoins, de votre positionnement et de vos objectifs pour definir le cahier des charges.'
        },
        {
            'number': '02',
            'title': 'Selection',
            'description': 'Identification des artisans et des pieces correspondant a vos criteres parmi notre reseau de partenaires.'
        },
        {
            'number': '03',
            'title': 'Echantillonnage',
            'description': 'Envoi d\'echantillons pour validation des materiaux, finitions et qualite avant production.'
        },
        {
            'number': '04',
            'title': 'Production',
            'description': 'Fabrication artisanale avec suivi qualite a chaque etape et reporting regulier.'
        },
        {
            'number': '05',
            'title': 'Expedition',
            'description': 'Conditionnement soigne, gestion douaniere et livraison a destination dans les delais convenus.'
        }
    ]
    return render_template('processus.html', steps=steps)


@business_bp.route('/faq')
def faq():
    faqs = [
        {
            'question': 'Quels sont vos delais de livraison ?',
            'answer': 'Les delais varient selon les produits et quantites. En general, comptez 4 a 8 semaines pour une commande standard, incluant la production artisanale et le transport international.'
        },
        {
            'question': 'Proposez-vous des creations sur mesure ?',
            'answer': 'Oui, nous travaillons avec nos artisans pour creer des pieces personnalisees selon vos specifications : dimensions, couleurs, motifs, materiaux.'
        },
        {
            'question': 'Quelles sont vos quantites minimales de commande ?',
            'answer': 'Les minimums varient selon les categories de produits. Pour les petits objets decoratifs, le minimum est generalement de 20 pieces. Pour le mobilier, nous acceptons des commandes a partir de 5 unites.'
        },
        {
            'question': 'Comment garantissez-vous la qualite ?',
            'answer': 'Chaque piece est inspectee avant expedition. Nous travaillons exclusivement avec des artisans selectionnes et formes a nos standards de qualite.'
        },
        {
            'question': 'Livrez-vous a l\'international ?',
            'answer': 'Oui, nous livrons dans le monde entier. Nous gerons l\'ensemble de la logistique : emballage, documentation douaniere, transport et livraison finale.'
        },
        {
            'question': 'Quels sont vos modes de paiement ?',
            'answer': 'Nous acceptons les virements bancaires et les lettres de credit pour les commandes importantes. Un acompte de 50% est demande a la commande.'
        }
    ]
    return render_template('faq.html', faqs=faqs)
