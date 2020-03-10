from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.errors import errors


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/product-database'
}

from resources.routes import initialize_routes

api = Api(app, errors=errors)

initialize_db(app)
initialize_routes(api)