# Generated by Django 3.2.4 on 2021-09-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0014_gasto_tipogasto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasto',
            name='cantidad',
            field=models.IntegerField(),
        ),
    ]
