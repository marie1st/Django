# Generated by Django 3.0 on 2020-07-27 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='stamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
