from django.db import models
from django.urls import reverse
from django.utils import timezone
from product.models import Product
from member.models import Member

# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.IntegerField('수량')
    total = models.IntegerField('합계금액')
    cart_date = models.DateTimeField('등록일', default=timezone.now)

    def __str__(self):
        return self.product_id

    def get_absolute_url(self):
        return reverse('cart:detail')
