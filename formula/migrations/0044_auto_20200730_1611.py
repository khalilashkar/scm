# Generated by Django 3.0.4 on 2020-07-30 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0043_auto_20200730_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docs',
            name='image',
            field=models.FileField(upload_to='documents/', verbose_name='ملف'),
        ),
    ]
