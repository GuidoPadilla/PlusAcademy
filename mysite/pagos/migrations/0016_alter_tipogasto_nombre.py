# Generated by Django 3.2.4 on 2021-09-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0015_alter_gasto_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipogasto',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
