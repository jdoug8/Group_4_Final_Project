from django.test import TestCase

# Create your tests here.
import unittest
from .models import Bid, Customer

class TestBid(unittest.TestCase):
    def setUp(self):
        # Creating a customer instance for testing
        self.customer = Customer('John Doe', 'johndoe@example.com')

    def test_get_customer_info(self):
        # Creating a job instance for testing
        bid = Bid(self.customer, 'web design')
        # Testing the get_customer_info method
        self.assertEqual(bid.get_customer_info(), 'John Doe (johndoe@example.com)')

if __name__ == '__main__':
    unittest.main()