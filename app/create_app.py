from flask import Flask
import json
from app import db
from app.models import Order, Offer, User


def load_data(path):
    with open(path, encoding = 'UTF-8') as file:
        return json.load(file)


def load_offer(path):
    offers = load_data(path)

    for offer in offers:
        db.session.add(
            Offer(
                id=offer.get("id"),
                order_id=offer.get("order_id"),
                executor_id=offer.get("executor_id")
            )
        )

        db.session.commit()


def load_order(path):
    orders = load_data(path)

    for order in orders:
        db.session.add(
            Order(
                id=order.get("id"),
                name=order.get("name"),
                description=order.get("description"),
                start_date=order.get("start_date"),
                end_date=order.get("end_date"),
                address=order.get("address"),
                price=order.get("price"),
                customer_id=order.get("customer_id"),
                executor_id=order.get("executor_id")
            )
        )

        db.session.commit()


def load_user(path):
    users = load_data(path)

    for user in users:
        db.session.add(
            User(
                id=user.get("id"),
                first_name=user.get("first_name"),
                last_name=user.get("last_name"),
                age=user.get("age"),
                email=user.get("email"),
                role=user.get("role"),
                phone=user.get("phone"),
            )
        )

        db.session.commit()


def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 4}
    app.config['SQLALCHEMY_ECHO'] = True

    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()
        offer = load_offer("data/offers.json")
        user = load_user("data/users.json")
        order = load_order("data/orders.json")

    return app


app = create_app()
