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