from flask import jsonify
from flask_restplus import Api, Resource, fields
from .app import app

api = Api(app, prefix="/api/v2", version='2.0', title='Fast-Foods-API', description="An API for ordering Fast Foods"

          )

user = api.model('User', {
    'username': fields.String(description="username", required=True, min_length=4),
     'password': fields.String(description="password", required=True, min_length=4)
})


orderobj = api.model('Order', {

    'meal': fields.String(description="meal to be ordered", required=True, min_length=4),
    'username': fields.String(description="name of person ordering meal", required=True, min_length=4),
    'location': fields.String(description="location of person ordering meal", required=True, min_length=4),
    'quantity': fields.Integer(description="quantity of meal required", required=True, min_length=4)
})

updateorder = api.model('Update Order Status', {
    'status': fields.String(description="Status of order", required=True, min_length=4)
})

fastfood=api.model('fastfood',{
    'meal_name': fields.String(description="username", required=True, min_length=4),
     'price': fields.String(description="password", required=True, min_length=4)
    })


@api.route('/auth/admin')
class Admin(Resource):
    @api.expect(user)
    def post(self):
      pass

@api.route('/auth/signup')
class SignUp(Resource):
    @api.expect(user,code=201)
    def post(self):
        """ Register user"""
        pass

@api.route('/auth/login')
class Login(Resource):
    @api.expect(user)
    def post(self):
        """Login User"""
        pass

# fastfoods
@api.route('/menu')
class Menu(Resource):
    @api.expect(fastfood)
    def post(self):
        """Add Meal Option"""
        pass

    def get(self):
        """Get Menu"""
        pass
    
@api.route('/menu/<int:meal_id>')
class Meal(Resource):
    @api.expect(fastfood)
    def put(self,meal_id):
        """update fastfood"""
        pass

    
    def delete(self,meal_id):
        """Delete FastFood"""
        pass

# orders
@api.route('/users/orders')
class UserOrders(Resource):
    def post(self):
        """ Post An Order"""
        pass

    def get(self):
        """Get orders of a specifi user"""
        pass

@api.route('/orders')
class Orders(Resource):
    def get(self):
        """GET all orders"""
        pass

@api.route('/orders/<int:orderId>')
class Order(Resource):
    def get(self,orderId):
        """GET A SPECIFIC ORDER"""
        pass

    @api.expect(updateorder)
    def put(self,orderId):
        """ Update order status"""
        pass
        

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
