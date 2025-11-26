class ProductService:
    def __init__(self):
        self._products = self._load_products()
        self._categories = self._load_categories()
    
    def _load_products(self):
        return [
            {
                'id': 1,
                'name': 'Ex-Votos en Laiton',
                'category': 'laiton',
                'description': 'Ex-votos decoratifs en laiton martele a la main, pieces uniques refletant le savoir-faire artisanal marocain.',
                'details': 'Chaque ex-voto est fabrique a la main par des artisans marocains. Le laiton est martele selon des techniques traditionnelles transmises de generation en generation.',
                'dimensions': 'Hauteur : 15-20 cm',
                'material': 'Laiton martele',
                'image': '/static/images/moroccan_brass_craft_91c1b440.jpg'
            },
            {
                'id': 2,
                'name': 'Miroirs Artisanaux',
                'category': 'decoration',
                'description': 'Miroirs ornementaux encadres a la main, inspires des motifs traditionnels marocains.',
                'details': 'Miroirs avec cadres en bois sculpte ou en laiton cisele, parfaits pour apporter une touche d\'elegance orientale.',
                'dimensions': 'Diametre : 30-40 cm',
                'material': 'Bois sculpte / Laiton',
                'image': '/static/images/moroccan_brass_craft_59d29144.jpg'
            },
            {
                'id': 3,
                'name': 'Mini Cadre Identite',
                'category': 'decoration',
                'description': 'Petit cadre decoratif en laiton, disponible en 2 modeles.',
                'details': 'Parfait pour mettre en valeur vos photos ou creer une composition murale artistique.',
                'dimensions': 'Timbre : H 5,5 x L 4,5 cm / Cadre : H 6,5 x L 4,5 cm',
                'material': 'Laiton',
                'image': '/static/images/moroccan_brass_craft_5197c08b.jpg'
            },
            {
                'id': 4,
                'name': 'Soliflore Mural en Laiton',
                'category': 'laiton',
                'description': 'Petit vase mural en laiton pour une fleur unique, design epure et elegant.',
                'details': 'Fixation murale discrete, ideal pour creer une decoration florale minimaliste.',
                'dimensions': 'Hauteur : 12 cm',
                'material': 'Laiton poli',
                'image': '/static/images/moroccan_brass_craft_8cacf1dc.jpg'
            },
            {
                'id': 5,
                'name': 'Mobiles Decoratifs en Laiton',
                'category': 'laiton',
                'description': 'Mobiles suspendus en laiton martele, creant un jeu de lumiere apaisant.',
                'details': 'Ces mobiles apportent mouvement et eclat a votre interieur, refletant la tradition du travail du laiton marocain.',
                'dimensions': 'Hauteur totale : 40-50 cm',
                'material': 'Laiton martele',
                'image': '/static/images/moroccan_brass_craft_af2c930a.jpg'
            },
            {
                'id': 6,
                'name': 'Boites et Bougeoirs',
                'category': 'laiton',
                'description': 'Ensemble de boites decoratives et bougeoirs en laiton cisele.',
                'details': 'Pieces artisanales aux motifs geometriques traditionnels, parfaites pour ranger petits objets ou creer une ambiance chaleureuse.',
                'dimensions': 'Variables selon modeles',
                'material': 'Laiton cisele',
                'image': '/static/images/moroccan_brass_craft_5cbdcb61.jpg'
            },
            {
                'id': 7,
                'name': 'Poteries Terre Cuite',
                'category': 'ceramique',
                'description': 'Poteries et jarres en terre cuite fabriquees selon les methodes ancestrales.',
                'details': 'Chaque piece est tournee a la main et cuite au four traditionnel. Parfait pour la decoration ou usage quotidien.',
                'dimensions': 'Hauteur : 20-30 cm',
                'material': 'Terre cuite naturelle',
                'image': '/static/images/moroccan_artisan_han_11a3ad05.jpg'
            },
            {
                'id': 8,
                'name': 'Trophees Animaux Decoratifs',
                'category': 'decoration',
                'description': 'Tetes d\'animaux decoratives en laiton ou metal recycle, style boheme chic.',
                'details': 'Sculptures murales uniques creees par des artisans marocains, alliant tradition et modernite.',
                'dimensions': 'Environ 25 x 20 cm',
                'material': 'Laiton / Metal recycle',
                'image': '/static/images/moroccan_artisan_han_43aa89bc.jpg'
            },
            {
                'id': 9,
                'name': 'Mobilier Bois et Tissages',
                'category': 'mobilier',
                'description': 'Pieces de mobilier en bois massif avec tissages artisanaux.',
                'details': 'Tables basses, etageres et assises combinant bois noble et textiles tisses a la main.',
                'dimensions': 'Variables selon modeles',
                'material': 'Bois massif, tissages coton/laine',
                'image': '/static/images/moroccan_artisan_han_0614122a.jpg'
            },
            {
                'id': 10,
                'name': 'Tapis et Assises',
                'category': 'textile',
                'description': 'Tapis berberes tisses main et poufs en cuir ou tissu brode.',
                'details': 'Tapis aux motifs geometriques traditionnels, poufs confortables pour creer un espace cosy.',
                'dimensions': 'Tapis : 120 x 180 cm / Poufs : diam 50 cm',
                'material': 'Laine / Coton / Cuir',
                'image': '/static/images/moroccan_artisan_han_2e2686eb.jpg'
            },
            {
                'id': 11,
                'name': 'Luminaires Appliques Murales',
                'category': 'luminaires',
                'description': 'Appliques murales en laiton ajoure, creant des jeux d\'ombres poetiques.',
                'details': 'Luminaires traditionnels marocains avec motifs ciseles, diffusant une lumiere douce et chaleureuse.',
                'dimensions': 'Hauteur : 30-40 cm',
                'material': 'Laiton cisele',
                'image': '/static/images/moroccan_brass_craft_91c1b440.jpg'
            },
            {
                'id': 12,
                'name': 'Paniers en Fibres Naturelles',
                'category': 'textile',
                'description': 'Paniers, sacs et chapeaux tresses en fibres naturelles (palmier, jonc).',
                'details': 'Vannerie traditionnelle marocaine, pratique et esthetique pour le quotidien.',
                'dimensions': 'Variables selon modeles',
                'material': 'Fibres naturelles tressees',
                'image': '/static/images/moroccan_brass_craft_59d29144.jpg'
            },
            {
                'id': 13,
                'name': 'Plateau en Laiton',
                'category': 'laiton',
                'description': 'Grand plateau en laiton cisele aux motifs geometriques traditionnels.',
                'details': 'Piece maitresse pour servir le the a la menthe ou decorer votre table basse.',
                'dimensions': 'Diametre : 40-50 cm',
                'material': 'Laiton cisele',
                'image': '/static/images/moroccan_brass_craft_5197c08b.jpg'
            },
            {
                'id': 14,
                'name': 'Vaisselle Artisanale',
                'category': 'ceramique',
                'description': 'Assiettes, bols et plats en ceramique peinte a la main.',
                'details': 'Ceramique de Fes ou Safi aux motifs colores traditionnels, chaque piece est unique.',
                'dimensions': 'Assiettes : diam 25 cm',
                'material': 'Ceramique emaillee',
                'image': '/static/images/moroccan_brass_craft_8cacf1dc.jpg'
            },
            {
                'id': 15,
                'name': 'Bracelets Maayaz',
                'category': 'bijoux',
                'description': 'Bracelets en fils d\'or tisses selon la methode traditionnelle de la sfifa.',
                'details': 'Chaque bracelet Maayaz est le fruit d\'un travail artisanal minutieux realise dans un atelier local au Maroc.',
                'dimensions': 'Ajustable : 14-23 cm',
                'material': 'Fils metallises (or, argent, cuivre)',
                'image': '/static/images/moroccan_brass_craft_af2c930a.jpg'
            },
            {
                'id': 16,
                'name': 'Poufs et Gros Coussins',
                'category': 'textile',
                'description': 'Poufs en cuir traditionnel et grands coussins brodes.',
                'details': 'Assises confortables garnies de mousse, revetements en cuir tanne ou tissus brodes main.',
                'dimensions': 'Poufs : diam 50 x H 35 cm',
                'material': 'Cuir / Tissus brodes',
                'image': '/static/images/moroccan_brass_craft_5cbdcb61.jpg'
            },
            {
                'id': 17,
                'name': 'Coussins Brodes',
                'category': 'textile',
                'description': 'Coussins en velours uni colore avec broderies traditionnelles.',
                'details': 'Housses de coussins faites main avec broderies aux fils de soie, couleurs chatoyantes.',
                'dimensions': '40 x 40 cm ou 50 x 50 cm',
                'material': 'Velours, coton, broderies soie',
                'image': '/static/images/moroccan_artisan_han_11a3ad05.jpg'
            },
            {
                'id': 18,
                'name': 'Pateres en Laiton',
                'category': 'laiton',
                'description': 'Pateres murales decoratives en laiton forge.',
                'details': 'Crochets muraux elegants pour suspendre vetements, sacs ou creer une composition decorative.',
                'dimensions': 'Longueur : 8-12 cm',
                'material': 'Laiton forge',
                'image': '/static/images/moroccan_artisan_han_43aa89bc.jpg'
            }
        ]
    
    def _load_categories(self):
        return [
            {'id': 'all', 'name': 'Tous les produits', 'icon': None},
            {'id': 'laiton', 'name': 'Laiton', 'icon': None},
            {'id': 'ceramique', 'name': 'Ceramique et Poterie', 'icon': None},
            {'id': 'textile', 'name': 'Textile et Tissage', 'icon': None},
            {'id': 'mobilier', 'name': 'Mobilier', 'icon': None},
            {'id': 'luminaires', 'name': 'Luminaires', 'icon': None},
            {'id': 'bijoux', 'name': 'Bijoux', 'icon': None},
            {'id': 'decoration', 'name': 'Decoration', 'icon': None}
        ]
    
    def get_all_products(self):
        return self._products
    
    def get_featured_products(self, limit=6):
        return self._products[:limit]
    
    def get_product_by_id(self, product_id):
        for product in self._products:
            if product['id'] == product_id:
                return product
        return None
    
    def get_categories(self):
        return self._categories
    
    def get_products_by_category(self, category_id):
        if category_id == 'all':
            return self._products
        return [p for p in self._products if p['category'] == category_id]
    
    def get_related_products(self, product, limit=4):
        related = [p for p in self._products if p['category'] == product['category'] and p['id'] != product['id']]
        return related[:limit]
