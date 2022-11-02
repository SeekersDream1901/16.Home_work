from flask import Blueprint, jsonify

from database.models.models import User, Order, Offer
from path import USERS_JSON, ORDERS_JSON, OFFERS_JSON
from utils import db_load

index_blueprint = Blueprint('index_blueprint', __name__)


@index_blueprint.before_app_first_request
def first_request():
    db_load(USERS_JSON, User)
    db_load(ORDERS_JSON, Order)
    db_load(OFFERS_JSON, Offer)


@index_blueprint.get('/')
def index_page():
    return jsonify({'status': 'ok'})
