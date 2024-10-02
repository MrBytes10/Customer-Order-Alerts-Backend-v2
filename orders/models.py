from django.db import models
import africastalking
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# customers API integration
class Customer(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15, default='+254780530990')

# africastalking API integration for SMS Notification on Order Creation
africastalking.initialize(username=os.getenv('AFRICASTALKING_USERNAME'), 
                          api_key=os.getenv('AFRICASTALKING_API_KEY'))  # Store credentials in environment variables
sms = africastalking.SMS

# orders API integration
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method first
        message = f"Order created for {self.customer.name}: {self.item} - {self.amount}"
        try:
            sms.send(message, [self.customer.phone_number])
        except Exception as e:
            # Log the error or handle it as necessary
            print(f"Error sending SMS: {e}")

