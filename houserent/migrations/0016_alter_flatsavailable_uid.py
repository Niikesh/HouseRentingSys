# Generated by Django 4.1 on 2023-12-01 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('houserent', '0015_alter_booking_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatsavailable',
            name='uid',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User Id'),
        ),
    ]