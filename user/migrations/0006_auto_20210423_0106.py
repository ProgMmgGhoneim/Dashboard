# Generated by Django 2.2 on 2021-04-23 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210422_0242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'managed': True, 'permissions': (('can_make_order', 'Can Make Order'),), 'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
    ]
