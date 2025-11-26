import os
import uuid
from PIL import Image
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def process_and_save_image(file, target_width=None, target_height=None, crop_data=None):
    if not file or not file.filename:
        return None
    
    if not allowed_file(file.filename):
        return None
    
    img = Image.open(file)
    
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    
    if crop_data:
        x = int(crop_data.get('x', 0))
        y = int(crop_data.get('y', 0))
        width = int(crop_data.get('width', img.width))
        height = int(crop_data.get('height', img.height))
        
        x = max(0, min(x, img.width))
        y = max(0, min(y, img.height))
        width = min(width, img.width - x)
        height = min(height, img.height - y)
        
        img = img.crop((x, y, x + width, y + height))
    
    if target_width and target_height:
        img = resize_and_crop(img, target_width, target_height)
    elif target_width:
        ratio = target_width / img.width
        new_height = int(img.height * ratio)
        img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
    elif target_height:
        ratio = target_height / img.height
        new_width = int(img.width * ratio)
        img = img.resize((new_width, target_height), Image.Resampling.LANCZOS)
    
    ext = file.filename.rsplit('.', 1)[1].lower()
    if ext == 'jpeg':
        ext = 'jpg'
    
    filename = secure_filename(f"{uuid.uuid4().hex}.{ext}")
    upload_dir = os.path.join('static', 'uploads')
    
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    
    filepath = os.path.join(upload_dir, filename)
    
    if ext in ('jpg', 'jpeg'):
        img.save(filepath, 'JPEG', quality=85, optimize=True)
    elif ext == 'png':
        img.save(filepath, 'PNG', optimize=True)
    elif ext == 'webp':
        img.save(filepath, 'WEBP', quality=85)
    else:
        img.save(filepath)
    
    return f"/static/uploads/{filename}"


def resize_and_crop(img, target_width, target_height):
    img_ratio = img.width / img.height
    target_ratio = target_width / target_height
    
    if img_ratio > target_ratio:
        new_height = target_height
        new_width = int(new_height * img_ratio)
    else:
        new_width = target_width
        new_height = int(new_width / img_ratio)
    
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    left = (new_width - target_width) // 2
    top = (new_height - target_height) // 2
    right = left + target_width
    bottom = top + target_height
    
    img = img.crop((left, top, right, bottom))
    
    return img


IMAGE_SIZES = {
    'hero_main': (800, 600),
    'hero_card': (400, 300),
    'product': (600, 600),
    'product_thumb': (300, 300),
    'testimonial': (100, 100),
    'og_image': (1200, 630),
    'logo': (200, 200),
}


def process_image_for_type(file, image_type, crop_data=None):
    if image_type in IMAGE_SIZES:
        width, height = IMAGE_SIZES[image_type]
        return process_and_save_image(file, target_width=width, target_height=height, crop_data=crop_data)
    return process_and_save_image(file, crop_data=crop_data)
