# Generated by Django 3.0.4 on 2020-07-29 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0024_violation_violation_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='date_of_violations_1',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='kind_of_violation_1',
        ),
    ]
