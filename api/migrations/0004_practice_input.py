# Generated by Django 3.2.9 on 2021-11-26 12:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_practice_input'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice',
            name='input',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), null=True, size=None), null=True, size=None),
        ),
    ]
