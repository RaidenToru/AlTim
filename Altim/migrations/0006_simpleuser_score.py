# Generated by Django 2.2.6 on 2019-12-10 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Altim', '0005_plane_plane_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleuser',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
