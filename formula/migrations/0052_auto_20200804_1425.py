# Generated by Django 3.0.4 on 2020-08-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0051_auto_20200804_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='list_of_tools',
            field=models.TextField(blank=True, max_length=255, null=True, verbose_name='إن كان الدعم المطلوب متعلق بمستلزمات خاصة بالعمل، نرجو تزويدنا بقائمة الأسعار'),
        ),
    ]
