# Generated by Django 3.2.7 on 2021-09-24 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_value_drinker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='drinks_num',
            field=models.IntegerField(max_length=100),
        ),
    ]
