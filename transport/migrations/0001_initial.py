# Generated by Django 4.2.4 on 2023-10-08 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdjustmentsSeatsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adjustments_seats_name', models.CharField(max_length=50, unique=True, verbose_name='регулировка сидений')),
            ],
            options={
                'verbose_name': 'регулировка сидения',
                'verbose_name_plural': 'регулировка сидений',
            },
        ),
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
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'объявление',
                'verbose_name_plural': 'объявления',
            },
        ),
        migrations.CreateModel(
            name='AnnouncementCarEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'комплектация',
                'verbose_name_plural': 'комплектации',
            },
        ),
        migrations.CreateModel(
            name='AnnouncementCarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(db_index=True, upload_to='transport', verbose_name='фотографии объявлений')),
            ],
            options={
                'verbose_name': 'фотографии автомобиля',
                'verbose_name_plural': 'фотографии автомобилей',
            },
        ),
        migrations.CreateModel(
            name='BlindSpotMonitoringSystemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blind_spot_monitoring_system_name', models.CharField(max_length=50, unique=True, verbose_name='система контроля слепых зон')),
            ],
            options={
                'verbose_name': 'система контроля слепых зон',
                'verbose_name_plural': 'системы контроля слепых зон',
            },
        ),
        migrations.CreateModel(
            name='BluetoothType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bluetooth_name', models.CharField(max_length=50, unique=True, verbose_name='bluetooth-система')),
            ],
            options={
                'verbose_name': 'bluetooth-система',
                'verbose_name_plural': 'bluetooth-системы',
            },
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
            name='BodyKitType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_kit_name', models.CharField(max_length=50, unique=True, verbose_name='обвес')),
            ],
            options={
                'verbose_name': 'обвес',
                'verbose_name_plural': 'обвесы',
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
            name='ClimateControlType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('climate_control_name', models.CharField(max_length=64, unique=True, verbose_name='климат-контроль')),
            ],
            options={
                'verbose_name': 'климат-контроль',
                'verbose_name_plural': 'климат-контроли',
            },
        ),
        migrations.CreateModel(
            name='CollisionAvoidanceSystemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collision_avoidance_system_name', models.CharField(max_length=50, unique=True, verbose_name='система избежания столкновений')),
            ],
            options={
                'verbose_name': 'система избежания столкновений',
                'verbose_name_plural': 'системы избежания столкновений',
            },
        ),
        migrations.CreateModel(
            name='ColorSalonCarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_salon_car_name', models.CharField(max_length=50, unique=True, verbose_name='цвет салона')),
            ],
            options={
                'verbose_name': 'цвет салона',
                'verbose_name_plural': 'цвета салона',
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
            name='HeadlightsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headlights_name', models.CharField(max_length=50, unique=True, verbose_name='тип фар')),
            ],
            options={
                'verbose_name': 'тип фар',
                'verbose_name_plural': 'типы фар',
            },
        ),
        migrations.CreateModel(
            name='HeatedSeatsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heated_seats_name', models.CharField(max_length=50, unique=True, verbose_name='подогрев сидений')),
            ],
            options={
                'verbose_name': 'подогрев сидения',
                'verbose_name_plural': 'подогрев сидений',
            },
        ),
        migrations.CreateModel(
            name='LaneDepartureWarningSystemType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lane_departure_warning_system_name', models.CharField(max_length=50, unique=True, verbose_name='система предупреждения о сходе с полосы')),
            ],
            options={
                'verbose_name': 'система предупреждения о сходе с полосы',
                'verbose_name_plural': 'системы предупреждения о сходе с полосы',
            },
        ),
        migrations.CreateModel(
            name='LightSensorType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('light_sensor_name', models.CharField(max_length=50, unique=True, verbose_name='датчик света')),
            ],
            options={
                'verbose_name': 'датчик света',
                'verbose_name_plural': 'датчики света',
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
            name='ParkingSensorsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_sensors_name', models.CharField(max_length=50, unique=True, verbose_name='датчик парковки')),
            ],
            options={
                'verbose_name': 'датчик парковки',
                'verbose_name_plural': 'датчики парковки',
            },
        ),
        migrations.CreateModel(
            name='RaisSensorType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rain_sensor_name', models.CharField(max_length=50, unique=True, verbose_name='датчик дождя')),
            ],
            options={
                'verbose_name': 'датчик дождя',
                'verbose_name_plural': 'датчики дождя',
            },
        ),
        migrations.CreateModel(
            name='RoofCarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roof_car_name', models.CharField(max_length=50, unique=True, verbose_name='тип крышы')),
            ],
            options={
                'verbose_name': 'тип крышы',
                'verbose_name_plural': 'типы крыш',
            },
        ),
        migrations.CreateModel(
            name='SalonCarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salon_car_name', models.CharField(max_length=50, unique=True, verbose_name='тип салона')),
            ],
            options={
                'verbose_name': 'тип салона',
                'verbose_name_plural': 'типы салона',
            },
        ),
        migrations.CreateModel(
            name='StartStopType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_stop_name', models.CharField(max_length=50, unique=True, verbose_name='система start-stop')),
            ],
            options={
                'verbose_name': 'система start-stop',
                'verbose_name_plural': 'системы start-stop',
            },
        ),
        migrations.CreateModel(
            name='TransmissionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transmission', models.CharField(max_length=20, unique=True, verbose_name='коробка передач')),
            ],
            options={
                'verbose_name': 'тип коробки передач',
                'verbose_name_plural': 'типы коробок передач',
            },
        ),
        migrations.CreateModel(
            name='VentilationSeatsType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ventilation_seats_name', models.CharField(max_length=50, unique=True, verbose_name='вентиляция сидений')),
            ],
            options={
                'verbose_name': 'вентиляция сидения',
                'verbose_name_plural': 'вентиляция сидений',
            },
        ),
        migrations.AddConstraint(
            model_name='ventilationseatstype',
            constraint=models.CheckConstraint(check=models.Q(('ventilation_seats_name__length__lte', 50)), name='ventilation_seats_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='ventilationseatstype',
            constraint=models.CheckConstraint(check=models.Q(('ventilation_seats_name__length__gte', 0)), name='ventilation_seats_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='transmissiontype',
            constraint=models.CheckConstraint(check=models.Q(('transmission__length__lte', 20)), name='transmission__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='transmissiontype',
            constraint=models.CheckConstraint(check=models.Q(('transmission__length__gte', 0)), name='transmission__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='startstoptype',
            constraint=models.CheckConstraint(check=models.Q(('start_stop_name__length__lte', 50)), name='start_stop_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='startstoptype',
            constraint=models.CheckConstraint(check=models.Q(('start_stop_name__length__gte', 0)), name='start_stop_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='saloncartype',
            constraint=models.CheckConstraint(check=models.Q(('salon_car_name__length__lte', 50)), name='salon_car_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='saloncartype',
            constraint=models.CheckConstraint(check=models.Q(('salon_car_name__length__gte', 0)), name='salon_car_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='roofcartype',
            constraint=models.CheckConstraint(check=models.Q(('roof_car_name__length__lte', 50)), name='roof_car_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='roofcartype',
            constraint=models.CheckConstraint(check=models.Q(('roof_car_name__length__gte', 0)), name='roof_car_name__gte'),
        ),
        migrations.AddConstraint(
            model_name='raissensortype',
            constraint=models.CheckConstraint(check=models.Q(('rain_sensor_name__length__lte', 50)), name='rain_sensor_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='raissensortype',
            constraint=models.CheckConstraint(check=models.Q(('rain_sensor_name__length__gte', 0)), name='rain_sensor_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='parkingsensorstype',
            constraint=models.CheckConstraint(check=models.Q(('parking_sensors_name__length__lte', 50)), name='parking_sensors_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='parkingsensorstype',
            constraint=models.CheckConstraint(check=models.Q(('parking_sensors_name__length__gte', 0)), name='parking_sensors_name__length__gte'),
        ),
        migrations.AddField(
            model_name='modelcar',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='models', to='transport.brandcar'),
        ),
        migrations.AddConstraint(
            model_name='lightsensortype',
            constraint=models.CheckConstraint(check=models.Q(('light_sensor_name__length__lte', 50)), name='light_sensor_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='lightsensortype',
            constraint=models.CheckConstraint(check=models.Q(('light_sensor_name__length__gte', 0)), name='light_sensor_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='lanedeparturewarningsystemtype',
            constraint=models.CheckConstraint(check=models.Q(('lane_departure_warning_system_name__length__lte', 50)), name='lane_departure_warning_system_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='lanedeparturewarningsystemtype',
            constraint=models.CheckConstraint(check=models.Q(('lane_departure_warning_system_name__length__gte', 0)), name='lane_departure_warning_system_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='heatedseatstype',
            constraint=models.CheckConstraint(check=models.Q(('heated_seats_name__length__lte', 50)), name='heated_seats_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='heatedseatstype',
            constraint=models.CheckConstraint(check=models.Q(('heated_seats_name__length__gte', 0)), name='heated_seats_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='headlightstype',
            constraint=models.CheckConstraint(check=models.Q(('headlights_name__length__lte', 50)), name='headlights_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='headlightstype',
            constraint=models.CheckConstraint(check=models.Q(('headlights_name__length__gte', 0)), name='headlights_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='enginetypecar',
            constraint=models.CheckConstraint(check=models.Q(('engine__length__lte', 20)), name='engine__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='enginetypecar',
            constraint=models.CheckConstraint(check=models.Q(('engine__length__gte', 0)), name='engine__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='driveunittype',
            constraint=models.CheckConstraint(check=models.Q(('drive_unit__length__lte', 20)), name='drive_unit__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='driveunittype',
            constraint=models.CheckConstraint(check=models.Q(('drive_unit__length__gte', 0)), name='drive_unit__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='colortype',
            constraint=models.CheckConstraint(check=models.Q(('color__length__lte', 50)), name='color__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='colortype',
            constraint=models.CheckConstraint(check=models.Q(('color__length__gte', 0)), name='color__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='colorsaloncartype',
            constraint=models.CheckConstraint(check=models.Q(('color_salon_car_name__length__lte', 50)), name='color_salon_car_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='colorsaloncartype',
            constraint=models.CheckConstraint(check=models.Q(('color_salon_car_name__length__gte', 0)), name='color_salon_car_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='collisionavoidancesystemtype',
            constraint=models.CheckConstraint(check=models.Q(('collision_avoidance_system_name__length__lte', 50)), name='collision_avoidance_system_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='collisionavoidancesystemtype',
            constraint=models.CheckConstraint(check=models.Q(('collision_avoidance_system_name__length__gte', 0)), name='collision_avoidance_system_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='climatecontroltype',
            constraint=models.CheckConstraint(check=models.Q(('climate_control_name__length__lte', 64)), name='climate_control_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='climatecontroltype',
            constraint=models.CheckConstraint(check=models.Q(('climate_control_name__length__gte', 0)), name='climate_control_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='brandcar',
            constraint=models.CheckConstraint(check=models.Q(('brand_name__length__lte', 50)), name='brand_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='brandcar',
            constraint=models.CheckConstraint(check=models.Q(('brand_name__length__gte', 0)), name='brand_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='bodytypecar',
            constraint=models.CheckConstraint(check=models.Q(('body_type__length__lte', 50)), name='body_type__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='bodytypecar',
            constraint=models.CheckConstraint(check=models.Q(('body_type__length__gte', 0)), name='body_type__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='bodykittype',
            constraint=models.CheckConstraint(check=models.Q(('body_kit_name__length__lte', 50)), name='body_kit_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='bodykittype',
            constraint=models.CheckConstraint(check=models.Q(('body_kit_name__length__gte', 0)), name='body_kit_name__length__gte'),
        ),
        migrations.AddField(
            model_name='bodycar',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bodies', to='transport.modelcar'),
        ),
        migrations.AddConstraint(
            model_name='bluetoothtype',
            constraint=models.CheckConstraint(check=models.Q(('bluetooth_name__length__lte', 50)), name='bluetooth_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='bluetoothtype',
            constraint=models.CheckConstraint(check=models.Q(('bluetooth_name__length__gte', 0)), name='bluetooth_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='blindspotmonitoringsystemtype',
            constraint=models.CheckConstraint(check=models.Q(('blind_spot_monitoring_system_name__length__lte', 50)), name='blind_spot_monitoring_system_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='blindspotmonitoringsystemtype',
            constraint=models.CheckConstraint(check=models.Q(('blind_spot_monitoring_system_name__length__gte', 0)), name='blind_spot_monitoring_system_name__length__gte'),
        ),
        migrations.AddField(
            model_name='announcementcarimage',
            name='announcement_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='transport.announcementcar'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='adjustments_seats_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.adjustmentsseatstype', verbose_name='регулировка сидений'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='blind_spot_monitoring_system_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='transport.blindspotmonitoringsystemtype', verbose_name='система контроля слепых зон'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='bluetooth_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.bluetoothtype', verbose_name='bluetooth-система'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='body_kit_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='transport.bodykittype', verbose_name='обвес'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='climate_control_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.climatecontroltype', verbose_name='климат-контроль'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='collision_avoidance_system_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='transport.collisionavoidancesystemtype', verbose_name='система избежания столкновений'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='color_salon_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.colorsaloncartype', verbose_name='цвет салона'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='equipment_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='equipment', to='transport.announcementcar', verbose_name='объявление'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='headlights_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.headlightstype', verbose_name='тип фар'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='heated_seats_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.heatedseatstype', verbose_name='подогрев сидений'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='lane_departure_warning_system_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='transport.lanedeparturewarningsystemtype', verbose_name='система предупреждения о сходе с полосы'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='light_sensor_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='transport.lightsensortype', verbose_name='датчик света'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='parking_sensors_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='transport.parkingsensorstype', verbose_name='датчики парковки'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='rain_sensor_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='transport.raissensortype', verbose_name='датчик дождя'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='roof_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='transport.roofcartype', verbose_name='тип крышы'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='salon_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transport.saloncartype', verbose_name='тип салона'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='start_stop_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='transport.startstoptype', verbose_name='start-stop система'),
        ),
        migrations.AddField(
            model_name='announcementcarequipment',
            name='ventilation_seats_car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='transport.ventilationseatstype', verbose_name='вентиляция сидений'),
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
            model_name='adjustmentsseatstype',
            constraint=models.CheckConstraint(check=models.Q(('adjustments_seats_name__length__lte', 50)), name='adjustments_seats_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='adjustmentsseatstype',
            constraint=models.CheckConstraint(check=models.Q(('adjustments_seats_name__length__gte', 0)), name='adjustments_seats_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='modelcar',
            constraint=models.CheckConstraint(check=models.Q(('model_name__length__lte', 50)), name='model_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='modelcar',
            constraint=models.CheckConstraint(check=models.Q(('model_name__length__gte', 0)), name='model_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='bodycar',
            constraint=models.CheckConstraint(check=models.Q(('body_name__length__lte', 50)), name='body_name__length__lte'),
        ),
        migrations.AddConstraint(
            model_name='bodycar',
            constraint=models.CheckConstraint(check=models.Q(('body_name__length__gte', 0)), name='body_name__length__gte'),
        ),
        migrations.AddConstraint(
            model_name='announcementcar',
            constraint=models.CheckConstraint(check=models.Q(('year_of_issue__lte', 2023)), name='year_of_issue__lte'),
        ),
        migrations.AddConstraint(
            model_name='announcementcar',
            constraint=models.CheckConstraint(check=models.Q(('engine_volume__gte', 0)), name='engine_volume__ge'),
        ),
    ]
