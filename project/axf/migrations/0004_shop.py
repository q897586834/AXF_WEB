# Generated by Django 2.1.1 on 2018-11-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0003_mustbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=20)),
                ('trackid', models.CharField(max_length=20)),
            ],
        ),
    ]
