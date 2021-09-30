from django.urls import path
from cart.views import *

app_name = 'cart'

urlpatterns = [
    path('', detail, name='detail'),
    path('add/<int:product_id>/', add, name='cart_add'),
    path('remove/<int:cart_id>/', remove, name='cart_remove'),
]