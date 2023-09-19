# Generated by Django 4.2.4 on 2023-09-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_index=True, max_length=200, verbose_name='имя пользователя')),
                ('email', models.EmailField(db_index=True, max_length=100, verbose_name='email')),
                ('password', models.CharField(db_index=True, max_length=200, verbose_name='пароль')),
            ],
        ),
    ]
