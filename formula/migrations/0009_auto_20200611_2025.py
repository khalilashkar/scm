# Generated by Django 3.0.4 on 2020-06-11 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0008_auto_20200611_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='job',
            field=models.CharField(blank=True, choices=[('0', 'مراسل/ة '), ('1', 'محرر/ة '), ('2', 'مصور/ة '), ('3', 'مراسل/ة حربي/ة '), ('4', 'مراسل/ة عسكري/ة '), ('5', 'كاتب/ة- مدير/ة المكتب الاعلامي '), ('6', ' رئيس/ة تحرير '), ('7', ' معد/ة تقارير '), ('8', ' سيناريست '), ('9', ' مدير/ة قسم الإنتاج '), ('10', '  منسق/ة إعلامي/ة  '), ('11', ' مونيتير '), ('12', 'مخرج/ة  '), ('13', '  منتج/ة - متحدث/ة إعلامي/ة'), ('14', '  عامل/ة في المجال الإعلامي '), ('15', ' ناشط/ة إعلامي/ة '), ('16', '  مقدم/ة برامج- مذيع/ة '), ('17', 'فنان/ة تشكيلي/ة '), ('18', 'ممثل/ة '), ('19', ' غير ذلك')], max_length=255, null=True, verbose_name='المهنة '),
        ),
    ]