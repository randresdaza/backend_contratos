# Generated by Django 4.0.6 on 2023-05-19 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0004_alter_user_id_rol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id_rol',
            new_name='rol',
        ),
    ]