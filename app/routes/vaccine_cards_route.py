from flask import Blueprint
from app.controllers import vaccine_cards_controller

bp = Blueprint("vaccinations", __name__, url_prefix="/vaccinations")

bp.get("")(vaccine_cards_controller.get_vaccine_cards)
bp.get("/<int:vaccine_cards_cpf>")(vaccine_cards_controller.get_vaccine_card_by_cpf)
bp.post("")(vaccine_cards_controller.create_vaccine_card)