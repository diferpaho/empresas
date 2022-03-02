# Generated by Django 2.2.13 on 2022-03-02 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=40)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('telephone', models.IntegerField()),
            ],
        ),
    ]