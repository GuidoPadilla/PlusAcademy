# Generated by Django 3.1.7 on 2021-08-28 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_auto_20210828_1121'),
        ('pagos', '0011_auto_20210827_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cobro',
            name='tipo_moneda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.moneda'),
        ),
        migrations.AlterField(
            model_name='pago',
            name='moneda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.moneda'),
        ),
        migrations.DeleteModel(
            name='Moneda',
        ),
    ]
