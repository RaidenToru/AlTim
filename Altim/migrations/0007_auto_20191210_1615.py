# Generated by Django 2.2.6 on 2019-12-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Altim', '0006_simpleuser_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpleuser',
            name='userImg',
            field=models.ImageField(default='/default/default_user.png', upload_to='user_avas/'),
        ),
    ]
