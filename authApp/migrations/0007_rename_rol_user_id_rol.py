# Generated by Django 4.0.6 on 2023-05-19 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0006_alter_user_rol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='rol',
            new_name='id_rol',
        ),
    ]