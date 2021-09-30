# Generated by Django 3.2.6 on 2021-08-24 08:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_rename_pro_proce_product_pro_price'),
        ('member', '0002_mem_mem_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(verbose_name='수량')),
                ('total', models.IntegerField(verbose_name='합계금액')),
                ('cart_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='등록일')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.mem')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]