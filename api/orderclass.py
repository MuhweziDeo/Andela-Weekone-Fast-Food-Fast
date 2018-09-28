from datetime import datetime
class Order(object):
	# init class
	def __init__(self):
		self.idcounter=2
		self.orders=[]

	def create_order(self,data):
		order=data
		order['orderId']=self.idcounter = self.idcounter + 1
		order['status']='pending'
		order['Date']=str(datetime.utcnow())
		order['meal']=data['meal'].strip()
		order['username']=data['username'].strip()
		order['location']=data['location'].strip()
		self.orders.append(order)
		return order,201
		
	def get_all_orders(self):
		if len(self.orders)>=1:
			return self.orders,200
		else:
			return {'message':'No orders placed',
			"Expected Order Format":{
			"meal":"string",
			"username":"string",
			"location":"string",
			"quantity":"integer"
			}
			},204
			
			

	def get_one_order(self,orderId):
		for order in self.orders:
			if order['orderId']==orderId:
				return order,200
		return {"message":"Order with id {} wasnt found four or four".format(orderId)}, 404

	def update_order(self,orderId,data):
		order=self.get_one_order(orderId)
		order_status=data
		order_status['status']=data['status'].strip()
		order.update(order_status)
		return order,200