# Generated by Django 3.0.4 on 2020-07-29 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0028_auto_20200729_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='region',
            field=models.CharField(max_length=255, null=True, verbose_name='المنطقة'),
        ),
    ]
