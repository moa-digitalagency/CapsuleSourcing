from flask import Blueprint

main_bp = Blueprint('main', __name__)
catalogue_bp = Blueprint('catalogue', __name__)
business_bp = Blueprint('business', __name__)

from routes.main import *
from routes.catalogue import *
from routes.business import *
