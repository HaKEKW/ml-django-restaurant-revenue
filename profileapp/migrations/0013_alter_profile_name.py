# Generated by Django 4.2.2 on 2023-07-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0012_alter_predictedmodel_big_cities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
    ]
