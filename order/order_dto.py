from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from chatbot_api.ext.db import db
# from chatbot_api.user.user_dto import User
# from chatbot_api.shop.shop_dto import Shop
# from chatbot_api.food.food_dto import Food
# from chatbot_api.review.review_dto import Review


class OrderDto(db.Model) :
    __tablename__='order'
    __table_args__={'mysql_collate':'utf8_general_ci'}

    order_id : int = db.Column(db.Integer, primary_key=True, index=True)
    order_time : int = db.Column(db.Integer)
    # order_time : str = db.Column(db.DateTime, server_default=db.func.now()) #수정
    order_cmnt : str = db.Column(db.String(200))
    userid : str = db.Column(db.String(20), db.ForeignKey('User.userid')) #수정
    shop_id : int = db.Column(db.Integer, db.ForeignKey('Shop.shop_id')) #수정
    food_id : int = db.Column(db.Integer, db.ForeignKey('Food.food_id')) #수정
    review_id : int = db.Column(db.Integer, db.ForeignKey('Review.review_id')) #수정

    def __init__(self, order_time, order_cmnt, userid, shop_id, food_id, review_id) :
        self.order_time = order_time
        self.order_cmnt = order_cmnt
        self.userid = userid
        self.shop_id = shop_id
        self.food_id = food_id
        self.review_id = review_id
   

    def __repr__(self):
        return f'order_id = {self.order_id},\
            order_time = {self.order_time},\
            order_cmnt = {self.order_cmnt},\
            userid = {self.userid},\
            shop_id = {self.shop_id},\
            food_id = {self.food_id},\
            review_id = {self.review_id}'

    @property
    def json(self):
        return {
            'order_id' : self.order_id,
            'order_time' : self.order_time,
            'order_cmnt' : self.order_cmnt,
            'userid' : self.userid,
            'shop_id' : self.shop_id,
            'food_id' : self.food_id,
            'review_id' : self.review_id
        }

    def save(self) :
        # update와 create를 모두 수행
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
