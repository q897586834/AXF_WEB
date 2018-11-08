# Generated by Django 2.1.1 on 2018-11-03 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0006_foodtypes_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userAccount', models.CharField(max_length=20, unique=True)),
                ('userPasswd', models.CharField(max_length=20)),
                ('userName', models.CharField(max_length=20)),
                ('userPhone', models.CharField(max_length=20)),
                ('userAdderss', models.CharField(max_length=100)),
                ('userImg', models.CharField(max_length=150)),
                ('userRank', models.IntegerField()),
                ('userToken', models.CharField(max_length=50)),
            ],
        ),
    ]
