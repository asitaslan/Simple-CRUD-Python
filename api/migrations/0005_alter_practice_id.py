# Generated by Django 3.2.9 on 2021-11-26 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_practice_input'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
