# Generated by Django 3.1.7 on 2021-03-26 21:15

from django.db import migrations
import netfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('route_manager', '0002_ipaddress_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipaddress',
            name='ip',
            field=netfields.fields.InetAddressField(max_length=39, unique=True),
        ),
    ]
