# Generated by Django 3.1.7 on 2021-09-02 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0012_auto_20210828_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='cobro',
            name='relacionado',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pagos.cobro'),
        ),
        migrations.DeleteModel(
            name='cobrosExtra',
        ),
    ]
