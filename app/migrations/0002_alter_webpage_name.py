# Generated by Django 4.2.1 on 2023-07-14 08:16

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(max_length=20, validators=[app.models.check_for_a]),
        ),
    ]
