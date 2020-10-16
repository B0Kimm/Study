from flask_restful import Resource, reqparse
from chatbot_api.order.order_dto import OrderDto
from chatbot_api.order.order_dao import OrderDao

class OrderApi(Resource):
    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('order_id', type=int, required=False, help='This field cannot be left blank')
        # 수정 
        parser.add_argument('order_time', type=int, required=False, help='This field cannot be left blank')
        # 수정 : this field can be the empty space
        parser.add_argument('order_cmnt', type=str, required=False, help='This field cannot be left blank')
        parser.add_argument('userid', type=str, required=False, help='This field cannot be left blank')
        parser.add_argument('shop_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('food_id', type=int, required=False, help='This field cannot be left blank')
        parser.add_argument('review_id', type=int, required=False, help='This field cannot be left blank')

    def get(self, time) :
        order = self.dao.fetch_by_time(time)
        if item: 
            return item.json()
        return {'message' : 'Order not found'}, 404



    # def get(self, id) :
    #     order = OrderDao.find_by_id

class Orders(Resource):
    def get(self) :
        return {'orders': list(map(lambda order: order.json(), OrderDao.fetch_all()))}