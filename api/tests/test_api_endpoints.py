import unittest
import json
from api.app import app


class TestAPI(unittest.TestCase):
	def setUp(self):
		self.app=app
		self.client=self.app.test_client()
		
		self.order={
		  
		  "meal": "pizza",
		  "user": "dee",
		  "location": "kla",
		  'status':'incomplete',
		  "quantity": 5
		}
		self.updateorder={
		'status':"complete"
		}

	def test_create_order(self):
		res=self.client.post('fastfoods/api/v1/orders',data=json.dumps(self.order),content_type='application/json')
		self.assertIn('pizza',str(res.data))
		self.assertEqual(res.status_code,201)
	