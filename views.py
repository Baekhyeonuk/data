from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from product.models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.conf import settings
import os
from cart.forms import AddProForm

class ProListView(ListView):
    model = Product
    ## 모델명(소문자)_list.html
    template_name = 'product/list.html'
    ## object_list 로 객체 반환

def detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    add_to_cart = AddProForm()
    return render(request, 'product/detail.html', {'product':product, 'add_to_cart':add_to_cart})
