# Generated by Django 4.1.11 on 2023-10-04 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=15)),
                ('zip_code', models.IntegerField(max_length=10)),
                ('service', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('number_hour', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('pets', models.CharField(max_length=10)),
                ('pet_number', models.IntegerField()),
            ],
        ),
    ]
