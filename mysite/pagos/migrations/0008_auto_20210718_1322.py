# Generated by Django 3.2.4 on 2021-07-18 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0007_eliminacionpagos_fecha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eliminacionpagos',
            old_name='fecha',
            new_name='fechaSolicitud',
        ),
        migrations.AddField(
            model_name='eliminacionpagos',
            name='fechaRespuesta',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
