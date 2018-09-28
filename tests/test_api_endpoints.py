import unittest
import json
from api.app import app


class TestAPI(unittest.TestCase):
	def setUp(self):
		self.app=app
		self.client=self.app.test_client()
		
		self.order={
		  
		  "meal": "pizza",
		  "username": "aggrey",
		  "location": "Bunga",
		  "quantity": 5
		}
		self.invalid_order={
			"meal": "pizza",
		  "username": "aggrey",
		  "location": "Bunga",
		  
		}
		self.invalid_order_length={
			"meal": "pi",
		  "username": "aggrey",
		  "location": "Bunga",
		  "quantity":5
		  
		}
		self.updateorder={
		'status':"complete"
		}

	def test_create_order(self):
		res=self.client.post('fastfoods/api/v1/orders',data=json.dumps(self.order),content_type='application/json')
		self.assertIn('pizza',str(res.data))
		self.assertEqual(res.status_code,201)

	def test_get_order(self):
		res=self.client.post('fastfoods/api/v1/orders',data=json.dumps(self.order),content_type='application/json')
		res_order=self.client.get('fastfoods/api/v1/orders/1')
		self.assertIn('1',str(res_order.data))

	def test_get_orders(self):
		res=self.client.post('fastfoods/api/v1/orders',data=json.dumps(self.order),content_type='application/json')
		res_orders=self.client.get('fastfoods/api/v1/orders')
		self.assertEqual(res_orders.status,'200 OK')

	def test_update_order(self):
		res=self.client.post('fastfoods/api/v1/orders',data=json.dumps(self.order),content_type='application/json')
		res_update=self.client.put('fastfoods/api/v1/orders/1',data=json.dumps(self.updateorder),content_type='application/json')
		self.assertIn('Order 1 updated',str(res_update.data))



		# res=self.client.post('fastfoods/api/v1/orders',data=json.dumps(self.order),content_type='application/json')
		# res_update_order=self.client.put('fastfoods/api/v1/orders/3',data=json.dumps(self.updateorder),content_type='application/json')
		# self.assertIn('Order 3 updated',str(res_update_order.data))
		# res_order=self.client.get('fastfoods/api/v1/orders/3')
		# self.assertIn('complete',str(res_order.data))

	def test_missing_parameter_in_create_order(self):
		res=self.client.post('fastfoods/api/v1/orders',data=json.dumps(self.invalid_order),content_type='application/json')
		self.assertIn("Input payload validation failed",str(res.data))
	def test_length_of_values_in_create_order(self):
		res=self.client.post('fastfoods/api/v1/orders',data=json.dumps(self.invalid_order_length),content_type='application/json')
		self.assertIn("Input payload validation failed",str(res.data))
		self.assertIn("is too short",str(res.data))
	def test_access_invalid_url(self):
		res=self.client.get('fastfoods/api/v1/orders/kkjadja')
		self.assertIn("Hey The URL you Tried to Acess Doesnt Exist on the server",str(res.data))
		
	def test_access_url(self):
		res=self.client.get('fastfoods/api/v1/orders')
		self.assertEqual(200,res.status_code)





