# Generated by Django 3.0.4 on 2020-06-11 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportorgchild',
            name='support1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formula.Support_descrption', verbose_name='الجهة الداعمة '),
        ),
    ]
