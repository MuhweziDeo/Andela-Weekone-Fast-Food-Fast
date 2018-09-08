import unittest
import json
from api.app import app


class TestAPI(unittest.TestCase):
	def setUp(self):
		self.app=app
		self.client=self.app.test_client()
		self.fastfood={
		  "id": 1,
		  "name": "pizza",
		  "price": 400
		}
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