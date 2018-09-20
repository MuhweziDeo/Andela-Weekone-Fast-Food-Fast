
class Order(object):
	# init class
	def __init__(self):
		self.idcounter=2
		self.orders=[
							
			{
			"meal": "pizza",
			"username": "dee",
			"location": "Bunga",
			"quantity": 4,
			"Date": "2018-09-16T18:22:23.408Z",
			"orderId": 1,
			"status": "pending"
			},

			{
			"meal": "Burger",
			"username": "Mendy",
			"location": "Gayaza",
			"quantity": 4,
			"Date": "2018-09-16T18:22:23.408Z",
			"orderId": 2,
			"status": "Rejected"
			}
		]

	def create_order(self,data):
		order=data
		order['orderId']=self.idcounter = self.idcounter + 1
		order['status']='pending'
		self.orders.append(order)
		return order
		
	def get_all_orders(self):
		return self.orders

	def get_one_order(self,orderId):
		for order in self.orders:
			if order['orderId']==orderId:
				return order
		return {"message":"Order with id {} wasnt found four or four".format(orderId)}, 404

	def update_order(self,orderId,data):
		order=self.get_one_order(orderId)
		order.update(data)
		return order