# Generated by Django 3.1 on 2020-08-30 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_auto_20200830_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='timing',
            field=models.TimeField(auto_now=True),
        ),
    ]