from flask import Flask
from flask_restful import Api
from chatbot_api.ext.db import url, db
from chatbot_api.ext.routes import initialize_routes
from chatbot_api.order.order_api import OrderApi, Orders

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

initialize_routes(api)

with app.app_context():
    db.create_all()
