# Generated by Django 3.2.6 on 2021-09-03 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Up',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('face', models.CharField(max_length=80)),
                ('sign', models.TextField()),
                ('num_fan', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
