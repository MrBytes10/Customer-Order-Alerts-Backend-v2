"""
URL configuration for order_alerts project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse(
        "Welcome to the OrderAlert System backend APIs!<br>"
        "For specific API endpoints, please navigate to "
        "<br>"
        "customersapi: <a href='http://127.0.0.1:8000/api/customers/'> http://127.0.0.1:8000/api/customers/ </a>, "
        "OR"  
        "<br>"
        "ordersapi: <a href='http://127.0.0.1:8000/api/orders/'> http://127.0.0.1:8000/api/orders/ </a>, etc."
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('orders.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', home),  # This will handle the root URL
]
