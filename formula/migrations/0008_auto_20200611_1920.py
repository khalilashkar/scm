# Generated by Django 3.0.4 on 2020-06-11 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0007_auto_20200611_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='educatton_level',
            field=models.CharField(blank=True, choices=[('0', 'الثانوي'), ('1', 'الجامعي'), ('2', 'ما بعد جامعي'), ('3', 'مادون الثانوي ')], max_length=255, null=True, verbose_name=' التحصيل العلمي   '),
        ),
    ]