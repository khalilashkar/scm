# Generated by Django 3.0.4 on 2020-07-30 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0045_auto_20200730_1622'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docs',
            old_name='image',
            new_name='doc',
        ),
    ]