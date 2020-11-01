# Generated by Django 3.1 on 2020-10-27 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Shop', '0003_auto_20201027_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertiles',
            name='Person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
