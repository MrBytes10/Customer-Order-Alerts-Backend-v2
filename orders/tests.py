from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Customer, Order
from django.contrib.auth.models import User
from unittest.mock import patch

# CustomerTestCase
class CustomerTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.customer_data = {'name': 'John Doe', 'code': 'JD123', 'phone_number': '+254780530990'}
        self.response = self.client.post(
            reverse('customer-create'),
            self.customer_data,
            format="json"
        )

    def test_customer_creation(self):
        customer = Customer.objects.get(name="John Doe")
        self.assertEqual(customer.code, "JD123")

    def test_customer_creation_via_api(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.get().name, 'John Doe')

# OrderTestCase
class OrderTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.customer = Customer.objects.create(name="John Doe", code="JD123", phone_number="+254780530990")
        self.order_data = {'customer': self.customer.id, 'item': 'Item1', 'amount': 100.00}
        self.response = self.client.post(
            reverse('order-create'),
            self.order_data,
            format="json"
        )

    def test_order_creation(self):
        order = Order.objects.get(item="Item1")
        self.assertEqual(order.amount, 100.00)

    def test_order_creation_via_api(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.get().amount, 100.00)

    @patch('africastalking.SMS.send')  # Ensure this path is correct
    def test_sms_sent_on_order_creation(self, mock_send):
        # Create an order to trigger the SMS sending
        order = Order.objects.create(customer=self.customer, item='Item1', amount=100.00)

        # Ensure the SMS sending logic is invoked
        mock_send.assert_called_once_with(
            f"Order created for John Doe: Item1 - {order.amount}",  # Use the order.amount directly
            [self.customer.phone_number]
        )
