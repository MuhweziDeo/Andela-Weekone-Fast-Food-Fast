from flask import jsonify
from flask_restplus import Api, Resource, fields
from .app import app
from .orderclass import Order

api = Api(app, prefix="/fastfoods/api/v1", version='1.0', title='Fast-Foods-API', description="An API for ordering Fast Foods"

          )

order = Order()

orderobj = api.model('Order', {

    'meal': fields.String(description="meal to be ordered", required=True, min_length=4),
    'username': fields.String(description="name of person ordering meal", required=True, min_length=4),
    'location': fields.String(description="location of person ordering meal", required=True, min_length=4),
    'quantity': fields.Integer(description="quantity of meal required", required=True, min_length=4)
})

updateorder = api.model('Update Order Status', {
    'status': fields.String(description="Status of order", required=True, min_length=4)
})


@api.route('/orders')
class Orders(Resource):

    @api.expect(orderobj, validate=True)
    def post(self):
        """Create an order """
        data = api.payload
        return order.create_order(data)

    def get(self):
        """ Get All Orders """
        return order.get_all_orders()


@api.route('/orders/<int:orderId>')
class OneOrder(Resource):

    def get(self, orderId):
        """ Get Details of an Order by orderId"""
        return order.get_one_order(orderId)

    @api.expect(updateorder, validate=True)
    def put(self, orderId):
        """ update order Status of an order"""
        data = api.payload
        order.update_order(orderId, data)
        return {'message': 'Order {} updated'.format(orderId)}


@api.errorhandler(AttributeError)
def error(AttributeError):
    return {'error': "You Tried To Update An Order That doesnt Exist"
            }, 400


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({'message': "Hey The URL you Tried to Acess Doesnt Exist on the server",
                    "Please Go to Home page": "https://fast-foods-api.herokuapp.com/fastfoods/api/v1/orders"}), 404


@api.errorhandler
def error_handler(error):
    return {'message': str(error)}, getattr(error, 'code', 500)
