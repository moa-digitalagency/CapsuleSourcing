import os
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

from routes import main_bp, catalogue_bp, business_bp

app.register_blueprint(main_bp)
app.register_blueprint(catalogue_bp)
app.register_blueprint(business_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
