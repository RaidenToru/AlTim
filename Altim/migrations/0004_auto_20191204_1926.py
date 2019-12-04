# Generated by Django 2.2.6 on 2019-12-04 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Altim', '0003_auto_20191204_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='flight_initial_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_initial_place', to='Altim.City'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_last_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flight_last_place', to='Altim.City'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Altim.Ticket'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
