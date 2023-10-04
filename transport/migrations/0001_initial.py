# Generated by Django 4.2.4 on 2023-10-04 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncementCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('year_of_issue', models.PositiveIntegerField(verbose_name='Год выпуска')),
                ('mileage', models.PositiveIntegerField(verbose_name='Пробег')),
                ('engine_volume', models.FloatField(verbose_name='Объём двигателя')),
                ('engine_power', models.PositiveIntegerField(verbose_name='Мощность двигателя(л/с)')),
                ('description', models.TextField(verbose_name='Описание')),
                ('equipment', models.TextField(verbose_name='Комплектация')),
                ('slug', models.SlugField(default=False, max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'объявление',
                'verbose_name_plural': 'объявления',
            },
        ),
        migrations.CreateModel(
            name='AnnouncementCarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to='transport', verbose_name='фотографии объявлений')),
            ],
        ),
        migrations.CreateModel(
            name='BodyCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_name', models.CharField(max_length=50, unique=True, verbose_name='кузов')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'кузов',
                'verbose_name_plural': 'кузова',
            },
        ),
        migrations.CreateModel(
            name='BodyTypeCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_type', models.CharField(max_length=50, unique=True, verbose_name='тип кузова')),
            ],
            options={
                'verbose_name': 'тип кузова',
                'verbose_name_plural': 'типы кузова',
            },
        ),
        migrations.CreateModel(
            name='BrandCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50, unique=True, verbose_name='марка')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'бренд',
                'verbose_name_plural': 'бренды',
            },
        ),
        migrations.CreateModel(
            name='ColorType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50, unique=True, verbose_name='цвет')),
            ],
            options={
                'verbose_name': 'цвет',
                'verbose_name_plural': 'цвета',
            },
        ),
        migrations.CreateModel(
            name='DriveUnitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drive_unit', models.CharField(max_length=20, unique=True, verbose_name='привод')),
            ],
            options={
                'verbose_name': 'тип привода',
                'verbose_name_plural': 'типы приводов',
            },
        ),
        migrations.CreateModel(
            name='EngineTypeCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine', models.CharField(max_length=20, unique=True, verbose_name='тип двигателя')),
            ],
            options={
                'verbose_name': 'тип двигателя',
                'verbose_name_plural': 'типы двигателей',
            },
        ),
        migrations.CreateModel(
            name='ModelCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=50, unique=True, verbose_name='модель')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'модель',
                'verbose_name_plural': 'модели',
            },
        ),
        migrations.CreateModel(
            name='TransmissionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transmission', models.CharField(max_length=20, unique=True, verbose_name='коробка передач')),
            ],
            options={
                'verbose_name': 'коробка передач',
                'verbose_name_plural': 'коробки передач',
            },
        ),
        migrations.AddConstraint(
            model_name='transmissiontype',
            constraint=models.CheckConstraint(check=models.Q(('transmission__lenght__lte', 20)), name='transmission__lenght__lte'),
        ),
        migrations.AddConstraint(
            model_name='transmissiontype',
            constraint=models.CheckConstraint(check=models.Q(('transmission__lenght__gte', 0)), name='transmission__lenght__gte'),
        ),
        migrations.AddField(
            model_name='modelcar',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='models', to='transport.brandcar'),
        ),
        migrations.AddConstraint(
            model_name='enginetypecar',
            constraint=models.CheckConstraint(check=models.Q(('engine__lenght__lte', 20)), name='engine__lenght__lte'),
        ),
        migrations.AddConstraint(
            model_name='enginetypecar',
            constraint=models.CheckConstraint(check=models.Q(('engine__lenght__gte', 0)), name='engine__lenght__gte'),
        ),
        migrations.AddConstraint(
            model_name='driveunittype',
            constraint=models.CheckConstraint(check=models.Q(('drive_unit__lenght__lte', 20)), name='drive_unit__lenght__lte'),
        ),
        migrations.AddConstraint(
            model_name='driveunittype',
            constraint=models.CheckConstraint(check=models.Q(('drive_unit__lenght__gte', 0)), name='drive_unit__lenght__gte'),
        ),
        migrations.AddConstraint(
            model_name='colortype',
            constraint=models.CheckConstraint(check=models.Q(('color__lenght__lte', 50)), name='color__lenght__lte'),
        ),
        migrations.AddConstraint(
            model_name='colortype',
            constraint=models.CheckConstraint(check=models.Q(('color__lenght__gte', 0)), name='color__lenght__gte'),
        ),
        migrations.AddConstraint(
            model_name='brandcar',
            constraint=models.CheckConstraint(check=models.Q(('brand_name__lenght__lte', 50)), name='brand_name__lenght__lte'),
        ),
        migrations.AddConstraint(
            model_name='brandcar',
            constraint=models.CheckConstraint(check=models.Q(('brand_name__lengt__gte', 0)), name='brand_name__lenght__gte'),
        ),
        migrations.AddConstraint(
            model_name='bodytypecar',
            constraint=models.CheckConstraint(check=models.Q(('body_type__lenght__lte', 50)), name='body_type__lenght__lte'),
        ),
        migrations.AddConstraint(
            model_name='bodytypecar',
            constraint=models.CheckConstraint(check=models.Q(('body_type__lenght__gte', 0)), name='body_type__lenght__gte'),
        ),
        migrations.AddField(
            model_name='bodycar',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bodies', to='transport.modelcar'),
        ),
        migrations.AddField(
            model_name='announcementcarimage',
            name='announcement_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='transport.announcementcar', verbose_name=''),
        ),
        migrations.AddField(
            model_name='announcementcar',
            name='car_body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.bodycar', verbose_name='кузов'),
        ),
        migrations.AddField(
            model_name='announcementcar',
            name='car_body_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.bodytypecar', verbose_name='тип кузова'),
        ),
        migrations.AddField(
            model_name='announcementcar',
            name='car_brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.brandcar', verbose_name='бренд'),
        ),
        migrations.AddField(
            model_name='announcementcar',
            name='car_color_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.colortype', verbose_name='цвет'),
        ),
        migrations.AddField(
            model_name='announcementcar',
            name='car_drive_unit_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.driveunittype', verbose_name='тип привода'),
        ),
        migrations.AddField(
            model_name='announcementcar',
            name='car_engine_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.enginetypecar', verbose_name='тип двигателя'),
        ),
        migrations.AddField(
            model_name='announcementcar',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.modelcar', verbose_name='модель'),
        ),
        migrations.AddField(
            model_name='announcementcar',
            name='car_transmission_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.transmissiontype', verbose_name='тип коробки передач'),
        ),
        migrations.AddConstraint(
            model_name='modelcar',
            constraint=models.CheckConstraint(check=models.Q(('model_name__lenght__lte', 50)), name='model_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='modelcar',
            constraint=models.CheckConstraint(check=models.Q(('model_name__lenght__gte', 0)), name='model_name__lenght__gte'),
        ),
        migrations.AddConstraint(
            model_name='bodycar',
            constraint=models.CheckConstraint(check=models.Q(('body_name__lenght__lte', 50)), name='body_name__lenght__lte'),
        ),
        migrations.AddConstraint(
            model_name='bodycar',
            constraint=models.CheckConstraint(check=models.Q(('body_name__lenght__gte', 0)), name='body_name__lenght__gte'),
        ),
        migrations.AddConstraint(
            model_name='announcementcar',
            constraint=models.CheckConstraint(check=models.Q(('year_of_issue__lte', 2023)), name='year_of_issue__lte'),
        ),
        migrations.AddConstraint(
            model_name='announcementcar',
            constraint=models.CheckConstraint(check=models.Q(('engine_volume__ge', 0)), name='engine_volume__ge'),
        ),
    ]
