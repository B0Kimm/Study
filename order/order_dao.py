from chatbot_api.ext.db import db


class OrderDao() :

    @classmethod
    def fetch_all(cls) :
        return cls.query.all()
    
    @classmethod
    def fetch_by_time(self, order_time) :
        return cls.query.filter_by(order_time == order_time).all()

    @classmethod
    def fetch_by_userid(self, userid) :
        return cls.query.filter_by(userid == userid).first()

    @classmethod
    def fetch_by_shop_id(self, shop_id):
        return cls.query.filter_by(shop_id == shop_id).first()

    @classmethod
    def fetch_by_food_id(self, food_id):
        return cls.query.filter_by(food_id == food_id).first()

    @classmethod
    def fetch_by_review_id(self, review_id):
        return cls.query.filter_by(review_id == review_id).first()



# dto는 json과 연동
# table 생성 => json으로 변동
