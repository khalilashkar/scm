# Generated by Django 3.0.4 on 2020-07-30 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0038_auto_20200729_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='document_1',
            field=models.ImageField(blank=True, null=True, upload_to='documents/', verbose_name='ملف 1'),
        ),
    ]
