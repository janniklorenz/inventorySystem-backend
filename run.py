from flask import Flask
from flask_cors import CORS

def create_app(config_filename):
    app = Flask(__name__)
    cors = CORS(app)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from models import db
    db.init_app(app)

    return app


app = create_app("config")

if __name__ == "__main__":
    app.run(debug=True, port=63828)



# https://www.codementor.io/dongido/how-to-build-restful-apis-with-python-and-flask-fh5x7zjrx
