# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import text
# from sqlalchemy.orm import relationship
#
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db: SQLAlchemy = SQLAlchemy(app)
#
#
# class User(db.Model):
#     __tablename__ = "user"
#
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String)
#     last_name = db.Column(db.String)
#     age = db.Column(db.Integer)
#     email = db.Column(db.String)
#     role = db.Column(db.String)
#     phone = db.Column(db.String)
#
#     #offer = relationship("Offer")
#     #order = relationship("Order")
#
#
# class Offer(db.Model):
#     __tablename__ = "offer"
#
#     id = db.Column(db.Integer, primary_key=True)
#     order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
#     executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#
#     order = db.relationship("Order")
#     user = db.relationship("User")
#
#
# class Order(db.Model):
#     __tablename__ = "order"
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     description = db.Column(db.String)
#     start_date = db.Column(db.Date)
#     end_date = db.Column(db.Date)
#     address = db.Column(db.String)
#     price_int = db.Column(db.Integer)
#     customer_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#     executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))
#
#     user = relationship("User")
#     offer = relationship("Offer")
#
#
# if __name__ == "__main__":
#     app.run("localhost", port=8080)