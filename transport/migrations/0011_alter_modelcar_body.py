# Generated by Django 4.2.4 on 2023-09-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0010_modelcar_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelcar',
            name='body',
            field=models.CharField(max_length=50, verbose_name='Модель'),
        ),
    ]
