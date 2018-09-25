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
	'quantity':fields.Integer(description="quantity of meal required",required=True)
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
		

@api.errorhandler
def error_handler(error):
    return {'message': str(error)}, getattr(error, 'code', 401)



