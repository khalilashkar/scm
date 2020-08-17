# Generated by Django 3.0.4 on 2020-06-11 18:30

from django.db import migrations, models
import formula.validators


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0009_auto_20200611_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='document_1',
            field=models.FileField(blank=True, null=True, upload_to='documents/', validators=[formula.validators.validate_file_extensison], verbose_name='ملف 1'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='document_2',
            field=models.FileField(blank=True, null=True, upload_to='documents/', validators=[formula.validators.validate_file_extensison], verbose_name='ملف 2'),
        ),
    ]
