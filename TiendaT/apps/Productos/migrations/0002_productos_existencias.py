# Generated by Django 2.1 on 2018-11-29 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='Existencias',
            field=models.IntegerField(default=0),
        ),
    ]
