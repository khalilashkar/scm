# Generated by Django 2.2.12 on 2020-08-11 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0058_registration_resource_prof'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='know_support_programme',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='كيف علمت ببرنامج الدعم ؟'),
        ),
    ]
