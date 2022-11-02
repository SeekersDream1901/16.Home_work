import json

from flask import Blueprint, request, jsonify

from database.models.models import Offer
from utils import DataBase

offers_blueprint = Blueprint('offers_blueprint', __name__, url_prefix='/offers')


@offers_blueprint.route('/', methods=["GET", "POST"])
def offers_page():

    if request.method == "GET":
        return jsonify([offer.as_dict() for offer in Offer.query.all()])

    if request.method == "POST":
        offer = json.loads(request.data)
        new_offer = DataBase(Offer).add_data(offer)
        return f"Offer с id:{new_offer['id']} создан"


@offers_blueprint.route('/<int:pk>', methods=["PUT", "GET", "DELETE"])
def offer_page(pk):

    if request.method == "GET":
        return jsonify(Offer.query.get(pk).as_dict())

    if request.method == "PUT":
        offer_data = json.loads(request.data)
        DataBase(Offer).put_offer(pk, offer_data)
        return f"Данные offer с id:{pk} обновлены"

    if request.method == "DELETE":
        DataBase(Offer).delete_data(pk)
        return f"Offer с id:{pk} удалён"
