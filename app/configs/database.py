from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

db = SQLAlchemy()

def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['JSON_SORT_KEYS'] = False

    db.init_app(app)

    app.db = db

    from app.models.vaccine_cards_model import VaccineCard