# Generated by Django 4.2.2 on 2023-07-02 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0010_alter_predictedmodel_open_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictedmodel',
            name='other',
        ),
    ]