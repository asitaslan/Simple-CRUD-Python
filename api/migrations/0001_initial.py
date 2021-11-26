# Generated by Django 3.2.9 on 2021-11-26 12:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.SlugField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('problem', models.CharField(max_length=400)),
                ('point', models.IntegerField()),
                ('level', models.CharField(max_length=25)),
                ('language', models.CharField(max_length=15)),
                ('input', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None)),
                ('expected_output', models.CharField(max_length=200)),
            ],
        ),
    ]
