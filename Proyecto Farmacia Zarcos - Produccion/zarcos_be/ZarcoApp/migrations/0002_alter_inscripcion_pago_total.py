# Generated by Django 3.2.8 on 2021-10-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZarcoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='pago_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
