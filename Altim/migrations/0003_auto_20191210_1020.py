# Generated by Django 2.2.6 on 2019-12-10 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Altim', '0002_auto_20191210_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flight',
            name='flight_rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='flight',
        ),
        migrations.AddField(
            model_name='plane',
            name='aircompany',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Altim.AirCompany'),
        ),
        migrations.AddField(
            model_name='plane',
            name='plane_rating',
            field=models.FloatField(default=0.0, verbose_name='rating of plane'),
        ),
        migrations.AddField(
            model_name='review',
            name='plane',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Altim.Plane'),
        ),
    ]
