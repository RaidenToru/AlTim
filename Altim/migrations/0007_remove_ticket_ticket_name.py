# Generated by Django 2.2.6 on 2019-11-28 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Altim', '0006_ticket_ticket_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_name',
        ),
    ]
