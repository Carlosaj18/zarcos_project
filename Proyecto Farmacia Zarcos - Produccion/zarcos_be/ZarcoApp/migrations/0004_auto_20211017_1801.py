# Generated by Django 3.2.8 on 2021-10-17 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ZarcoApp', '0003_auto_20211017_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evento',
            old_name='categoria_FK_id',
            new_name='categoria_FK',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='lugar_FK_id',
            new_name='lugar_FK',
        ),
        migrations.RenameField(
            model_name='evento',
            old_name='tipoEvento_FK_id',
            new_name='tipoEvento_FK',
        ),
    ]
