# Generated by Django 3.0.4 on 2020-07-29 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0025_auto_20200729_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='violation',
            name='violation_type',
            field=models.CharField(choices=[('0', ' اعتقال'), ('1', 'اختطاف'), ('2', 'منع من العمل'), ('3', 'مصادرة معدات'), ('4', 'اعتداء بالضرب'), ('5', 'اصابة'), ('6', 'تهديد'), ('7', 'ابتزاز'), ('8', 'غير ذلك')], max_length=200, null=True, verbose_name='نوع الانتهاك'),
        ),
    ]
