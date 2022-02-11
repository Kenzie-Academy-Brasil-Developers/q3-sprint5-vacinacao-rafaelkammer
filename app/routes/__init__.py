from flask import Blueprint, Flask
from app.routes.vaccine_cards_route import bp as bp_vaccine_cards

bp_api = Blueprint("api", __name__, url_prefix="")

def init_app(app: Flask):
    bp_api.register_blueprint(bp_vaccine_cards)

    app.register_blueprint(bp_api)
