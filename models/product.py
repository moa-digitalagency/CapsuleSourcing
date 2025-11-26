class Product:
    def __init__(self, id, name, category, description, details, dimensions, material, image):
        self.id = id
        self.name = name
        self.category = category
        self.description = description
        self.details = details
        self.dimensions = dimensions
        self.material = material
        self.image = image
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'details': self.details,
            'dimensions': self.dimensions,
            'material': self.material,
            'image': self.image
        }


class Category:
    def __init__(self, id, name, icon=None):
        self.id = id
        self.name = name
        self.icon = icon
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'icon': self.icon
        }
