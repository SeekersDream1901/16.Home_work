import json

from flask import Blueprint, request, jsonify

from database.models.models import User
from utils import DataBase

users_blueprint = Blueprint('users_blueprint', __name__, url_prefix='/users')


@users_blueprint.route('/', methods=["GET", "POST"])
def users_page():

    if request.method == "GET":
        return jsonify([user.as_dict() for user in User.query.all()])

    if request.method == "POST":
        user = json.loads(request.data)
        new_user = DataBase(User).add_data(user)
        return f"Пользователь с id:{new_user['id']} создан"


@users_blueprint.route('/<int:pk>', methods=["PUT", "GET", "DELETE"])
def user_page(pk):

    if request.method == "GET":
        return jsonify(User.query.get(pk).as_dict())

    if request.method == "PUT":
        user_data = json.loads(request.data)
        DataBase(User).put_user(pk, user_data)
        return f"Данные пользователя с id:{pk} обновлены"

    if request.method == "DELETE":
        DataBase(User).delete_data(pk)
        return f"Пользователь с id:{pk} удалён"
