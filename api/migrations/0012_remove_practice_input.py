# Generated by Django 3.2.9 on 2021-11-26 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_practice_input'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='practice',
            name='input',
        ),
    ]
