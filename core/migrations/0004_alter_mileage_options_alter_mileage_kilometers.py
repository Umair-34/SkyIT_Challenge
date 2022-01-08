# Generated by Django 4.0 on 2022-01-07 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mileage',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterField(
            model_name='mileage',
            name='kilometers',
            field=models.PositiveIntegerField(verbose_name='mileage'),
        ),
    ]