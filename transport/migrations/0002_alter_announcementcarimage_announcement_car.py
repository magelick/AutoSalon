# Generated by Django 4.2.4 on 2023-10-09 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcementcarimage',
            name='announcement_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='transport.announcementcar'),
        ),
    ]
