# Generated by Django 3.1 on 2020-08-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_auto_20200830_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='timing',
            field=models.DateTimeField(choices=[('2020-09-30T10:00:00Z', '2020-09-30T10:00:00Z'), ('2020-09-30T12:00:00Z', '2020-09-30T12:00:00Z'), ('2020-09-30T16:00:00Z', '2020-09-30T16:00:00Z'), ('2020-09-30T19:00:00Z', '2020-09-30T19:00:00Z')], default='2020-09-30T10:00:00Z'),
        ),
    ]
