# Generated by Django 4.0.6 on 2022-07-18 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pasteleria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='venta',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='pasteleria.venta'),
            preserve_default=False,
        ),
    ]