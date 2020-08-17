# Generated by Django 2.2.12 on 2020-08-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0056_violation_responsibility'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='experience',
            field=models.CharField(blank=True, choices=[('0', 'لا'), ('1', 'نعم')], max_length=100, null=True, verbose_name='هل سبق عملت بأجر أو لديك خبرات سابقة ؟'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='type_of_dmande',
            field=models.CharField(blank=True, choices=[('0', 'مناصرة'), ('1', 'إيجاد فرصة عمل'), ('2', 'دعم قانوني'), ('3', 'دعم طبي'), ('4', 'دعم ملف اللجوء - تأشيرات خروج'), ('5', 'دعم الانتقال اﻵمن'), ('6', 'الدعم المعيشي'), ('7', 'الدعم التقني'), ('8', 'دعم بطاقات صحفية'), ('9', 'رسائل توصية'), ('10', 'خروج آمن'), ('11', 'غير ذلك')], max_length=30, null=True, verbose_name='طبيعة المساعدة المطلوبة'),
        ),
    ]
