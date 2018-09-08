from flask_restplus import Api,Resource,fields
from .app import app
from .orderclass import Order

api=Api(app, prefix="/fastfoods/api/v1")

order=Order()

orderobj=api.model('Order',{
	
	'meal':fields.String,
	'user':fields.String,
	'location':fields.String,
	'quantity':fields.Integer
	})

@api.route('/orders')
class Orders(Resource):

	@api.expect(orderobj)
	def post(self):
		data=api.payload
		return order.create_order(data),201

	def get(self):
		return order.get_all_orders()

@api.route('/orders/<int:orderId>')
class OneOrder(Resource):
	def get(self,orderId):
		return order.get_one_order(orderId)