# Generated by Django 2.2.12 on 2020-08-11 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0057_auto_20200811_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='resource_prof',
            field=models.CharField(blank=True, choices=[('0', 'لا'), ('1', 'نعم')], max_length=100, null=True, verbose_name='هل لديك مصادر تثبت عملك ؟'),
        ),
    ]
