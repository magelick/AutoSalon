# Generated by Django 4.2.4 on 2023-08-30 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='Марка')),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ModelCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('slug', models.SlugField(max_length=100)),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('mileage', models.PositiveIntegerField(verbose_name='Пробег')),
                ('year_of_issue', models.DateField(verbose_name='Год выпуска')),
                ('engine_type', models.CharField(max_length=20, verbose_name='Тип двигателя')),
                ('engine_volume', models.FloatField(verbose_name='Объём двигателя')),
                ('engine_power', models.PositiveIntegerField(verbose_name='Мощность двигателя(л/с)')),
                ('transmission', models.CharField(max_length=20, verbose_name='Коробка передач')),
                ('drive_unit', models.CharField(max_length=20, verbose_name='Привод')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('description', models.TextField(verbose_name='Описание')),
                ('brand_car', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.brandcar')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]
