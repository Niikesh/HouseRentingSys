# Generated by Django 4.1 on 2023-12-01 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houserent', '0016_alter_flatsavailable_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='status',
        ),
    ]
