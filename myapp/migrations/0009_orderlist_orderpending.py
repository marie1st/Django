# Generated by Django 3.0 on 2020-09-03 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0008_profile_cartquan'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(max_length=100)),
                ('productid', models.CharField(max_length=100)),
                ('productname', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderPending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('shipping', models.CharField(max_length=100)),
                ('payment', models.CharField(max_length=100)),
                ('other', models.TextField()),
                ('stamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('slip', models.ImageField(blank=True, null=True, upload_to='slip')),
                ('paymentid', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
