# Generated by Django 3.1 on 2020-08-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('PhoneNo', models.CharField(max_length=10)),
                ('timing', models.DateTimeField()),
                ('booking_time', models.DateTimeField(auto_now_add=True)),
                ('is_expired', models.BooleanField(default=True)),
            ],
        ),
    ]
