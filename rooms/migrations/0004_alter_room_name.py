# Generated by Django 4.1 on 2022-09-13 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(default='defalut', max_length=150),
        ),
    ]
