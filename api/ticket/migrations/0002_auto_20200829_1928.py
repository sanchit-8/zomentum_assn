# Generated by Django 3.1 on 2020-08-29 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='is_expired',
            field=models.BooleanField(default=False),
        ),
    ]