import json
import os

from sqlalchemy.exc import IntegrityError

from database.create_db import db


def load_json(file_json):
    """Чтение данных из json-файла"""
    with open(file_json, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def db_load(file_json, model):
    """Загрузка данных в БД"""
    db.create_all()
    data = load_json(os.path.join('data', file_json))
    table = [model(**i) for i in data]
    db.session.add_all(table)
    try:
        db.session.commit()
    except IntegrityError:
        print('База уже создана')
    db.session.close()


class DataBase:
    """
    Класс для работы с БД
    """
    def __init__(self, db_model):
        self.db_model = db_model

    def add_data(self, data):
        """
        Метод для добавления информации в БД
        :param data:
        :return:
        """
        new_object = self.db_model(**data)
        db.session.add(new_object)
        db.session.commit()
        return new_object.as_dict()

    def put_user(self, pk, user_data):
        """Метод для обновления данных user в БД"""
        user_id = self.db_model.query.get(pk)

        user_id.first_name = user_data["first_name"]
        user_id.last_name = user_data["last_name"]
        user_id.age = user_data["age"]
        user_id.email = user_data["email"]
        user_id.role = user_data["role"]
        user_id.phone = user_data["phone"]

        db.session.add(user_id)
        db.session.commit()
        return "User is put"

    def put_order(self, pk, order_data):
        """Метод для обновления данных order в БД"""
        order_id = self.db_model.query.get(pk)

        order_id.name = order_data["name"]
        order_id.description = order_data["description"]
        order_id.start_date = order_data["start_date"]
        order_id.end_date = order_data["end_date"]
        order_id.address = order_data["address"]
        order_id.price = order_data["price"]
        order_id.customer_id = order_data["customer_id"]
        order_id.executor_id = order_data["executor_id"]

        db.session.add(order_id)
        db.session.commit()
        return "Order is put"

    def put_offer(self, pk, offer_data):
        """Метод для обновления данных offer в БД"""
        offer_id = self.db_model.query.get(pk)

        offer_id.order_id = offer_data["order_id"]
        offer_id.executor_id = offer_data["executor_id"]

        db.session.add(offer_id)
        db.session.commit()
        return "Offer is put"

    def delete_data(self, pk):
        """Метод для удаления данных из БД"""
        data = self.db_model.query.get(pk)
        db.session.delete(data)
        db.session.commit()
