# Generated by Django 4.2.4 on 2023-09-19 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_email_alter_user_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
