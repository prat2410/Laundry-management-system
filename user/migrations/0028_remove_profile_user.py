# Generated by Django 4.2.3 on 2023-08-01 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_remove_profile_uuid_profile_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]