# Generated by Django 3.0.4 on 2020-06-11 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0011_auto_20200611_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='violations',
            field=models.CharField(blank=True, choices=[('0', 'نعم'), ('1', 'لا')], max_length=255, null=True, verbose_name=' هل سبق أن تعرضت لأي نوع من أنواع الانتهاكات؟'),
        ),
    ]
