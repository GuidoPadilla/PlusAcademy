# Generated by Django 3.2.4 on 2021-08-07 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0009_formapago'),
    ]

    operations = [
        migrations.AddField(
            model_name='pago',
            name='forma_pago',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pagos.formapago'),
        ),
    ]
