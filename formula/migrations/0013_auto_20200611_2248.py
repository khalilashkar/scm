# Generated by Django 3.0.4 on 2020-06-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0012_auto_20200611_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='relation_with_org',
            field=models.CharField(blank=True, choices=[('0', 'نعم'), ('1', 'لا')], max_length=255, null=True, verbose_name='هل لديك أي ارتباطات تنظيمية مع أي فصيل عسكري أو ديني أو تجمع سياسي أو ديني؟'),
        ),
    ]