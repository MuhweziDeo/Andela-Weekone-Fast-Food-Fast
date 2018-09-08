class Order(object):
	# init class
	def __init__(self):
		self.idcounter=0
		self.orders=[]

	def create_order(self,data):
		order=data
		order['orderId']=self.idcounter = self.idcounter + 1
		self.orders.append(order)
		return order
	def get_all_orders(self):
		return self.orders
	def get_one_order(self,orderId):
		for order in self.orders:
			if order['orderId']==id:
				return order
		return {"message":"Order with id {} wasnt found four or four".format(orderId)}, 404