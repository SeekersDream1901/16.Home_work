import json

from flask import Blueprint, request, jsonify

from database.models.models import Order
from utils import DataBase

orders_blueprint = Blueprint('orders_blueprint', __name__, url_prefix='/orders')


@orders_blueprint.route('/', methods=["GET", "POST"])
def orders_page():

    if request.method == "GET":
        return jsonify([order.as_dict() for order in Order.query.all()])

    if request.method == "POST":
        order = json.loads(request.data)
        new_order = DataBase(Order).add_data(order)
        return f"Заказ с id:{new_order['id']} создан"


@orders_blueprint.route('/<int:pk>', methods=["PUT", "GET", "DELETE"])
def order_page(pk):

    if request.method == "GET":
        return jsonify(Order.query.get(pk).as_dict())

    if request.method == "PUT":
        order_data = json.loads(request.data)
        DataBase(Order).put_order(pk, order_data)
        return f"Данные заказа с id:{pk} обновлены"

    if request.method == "DELETE":
        DataBase(Order).delete_data(pk)
        return f"Заказ с id:{pk} удалён"
