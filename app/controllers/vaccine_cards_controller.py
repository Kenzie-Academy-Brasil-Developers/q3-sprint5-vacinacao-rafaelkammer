from sqlalchemy.orm.session import Session
from flask import request, jsonify

from http import HTTPStatus
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import IntegrityError

from app.models.vaccine_cards_model import VaccineCard
from app.configs.database import db


def get_vaccine_card_by_cpf(call_vaccine_card_cpf: int):
    session: Session = db.session
    base_query = session.query(VaccineCard)
    try:
        vaccine_card = base_query.filter_by(cpf=call_vaccine_card_cpf).first_or_404(
            description="cpf not found"
        )
    except NotFound as e:
        return {"error": e.description}, HTTPStatus.NOT_FOUND

    return jsonify(vaccine_card), HTTPStatus.OK


def get_vaccine_cards():
    session: Session = db.session
    base_query = session.query(VaccineCard)

    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 3, type=int)
    vaccine_cards = base_query.order_by(VaccineCard.cpf).paginate(page, per_page)

    return jsonify(vaccine_cards.items), HTTPStatus.OK


def create_vaccine_card():
    data = request.get_json()

    if len(data["cpf"]) != 11:
        return {"error": "Wrong CPF format"}, HTTPStatus.BAD_REQUEST

    for value in data.values():
        if type(value) != type("string"):
            return {"error": "All fields must be on string format"}, HTTPStatus.BAD_REQUEST
    
    default_keys = ["cpf", "name", "vaccine_name", "health_unit_name"]

    for key in default_keys:
        if key not in data.keys():
            return {"error": "Incomplete request, check all fields"}, HTTPStatus.BAD_REQUEST

    try:
        vaccine_card = VaccineCard(**data)

        db.session.add(vaccine_card)
        db.session.commit()

    except IntegrityError:
        return {"error": "CPF already registred"}, HTTPStatus.CONFLICT
    
    return jsonify(vaccine_card), HTTPStatus.CREATED
