from flask_restplus import Api,Resource,fields
from .app import app
from .orderclass import Order

api=Api(app, prefix="/fastfoods/api/v1",version='1.0', title='Fast-Foods-API', description="An API for ordering Fast Foods"

	)

order=Order()

orderobj=api.model('Order',{
	
	'meal':fields.String(description="meal to be ordered",required=True),
	'username':fields.String(description="name of person ordering meal",required=True),
	'location':fields.String(description="location of person ordering meal",required=True),
	'quantity':fields.Integer(description="quantity of meal required",required=True),
	'Date': fields.DateTime(dt_format='rfc822'),
	})

updateorder=api.model('Update Order Status',{
	'status':fields.String(description="Status of order", required=True)
	})

@api.route('/orders')
class Orders(Resource):

	@api.expect(orderobj)
	def post(self):
		"""Create an order """
		data=api.payload
		if validate_order(data):
			return order.create_order(data),201
		else:
			return {'Info Message':'Missing Some Parameters',
			"Exepected input":{
						  "meal": "string",
						  "username": "string",
						  "location": "string",
						  "quantity": 0,
						  "Date": "2018-09-19T15:32:14.610Z"
						}
			}
		return order.create_order(data),201

	def get(self):
		""" Get All Orders """
		return order.get_all_orders()

@api.route('/orders/<int:orderId>')
class OneOrder(Resource):
	def get(self,orderId):
		""" Get Details of an Order by orderId"""
		return order.get_one_order(orderId)

	@api.expect(updateorder)	
	def put(self,orderId):
		""" update order Status of an order"""
		data=api.payload
		order.update_order(orderId,data)
		return {'message':'Order {} updated'.format(orderId)}
		
def validate_order(data):
	if "meal" in data and "location" in data and "username" in data and "quantity" in data:
		return True
	else:
		return False
	