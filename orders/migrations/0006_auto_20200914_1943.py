# Generated by Django 2.2.12 on 2020-09-14 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200914_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billing_address_final',
        ),
        migrations.RemoveField(
            model_name='order',
            name='shipping_address_final',
        ),
    ]
