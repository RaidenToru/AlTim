# Generated by Django 2.2.6 on 2019-12-10 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Altim', '0003_auto_20191210_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review_image',
        ),
    ]
