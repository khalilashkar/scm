# Generated by Django 3.0.4 on 2020-07-20 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0018_auto_20200612_0405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='document_1',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='document_2',
        ),
    ]
