from django.urls import path
from .views import CustomerCreateView, OrderCreateView

urlpatterns = [
    path('customers/', CustomerCreateView.as_view(), name='customer-create'),
    path('orders/', OrderCreateView.as_view(), name='order-create'),
]