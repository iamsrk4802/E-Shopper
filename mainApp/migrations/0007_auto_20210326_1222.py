# Generated by Django 3.1.7 on 2021-03-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='color',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.CharField(default=None, max_length=10),
        ),
    ]