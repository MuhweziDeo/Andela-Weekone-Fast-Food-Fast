class Order(object):
	# init class
	def __init__(self):
		self.idcounter=0
		self.orders=[]

	def create_order(self,data):
		order=data
		order['id']=self.idcounter = self.idcounter + 1
		self.orders.append(order)
		return order
	def get_all_orders(self):
		return self.orders
	def get_one_order(self,id):
		for order in self.orders:
			if order['id']==id:
				return order
		return {"message":"Order with id {} wasnt found four or four".format(id)}, 404