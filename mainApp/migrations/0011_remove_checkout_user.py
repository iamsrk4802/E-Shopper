# Generated by Django 3.1.7 on 2021-03-30 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_auto_20210330_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='user',
        ),
    ]