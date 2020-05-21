# Generated by Django 3.0.6 on 2020-05-21 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200520_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='NapravlenieStudenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iofglavnyi_st', models.CharField(max_length=100)),
                ('ys', models.DateTimeField()),
                ('yf', models.DateTimeField()),
                ('gruppa', models.CharField(max_length=100)),
                ('cel_poezdki', models.CharField(max_length=100)),
                ('df', models.DateTimeField()),
                ('mf', models.DateTimeField()),
                ('ds', models.DateTimeField()),
                ('dolzn_podrazd_st', models.CharField(max_length=100)),
                ('ms', models.DateTimeField()),
                ('fiofull', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='osnovnye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesto_naznacheniya', models.CharField(max_length=100)),
                ('naselennyj_punkt', models.CharField(max_length=100)),
                ('nazvanie_meropriyatie', models.CharField(max_length=100)),
                ('daystart', models.DateTimeField()),
                ('dayend', models.DateTimeField()),
                ('forma_obucheniya', models.CharField(max_length=100)),
                ('osnova_obucheniya', models.CharField(max_length=100)),
                ('table_spisokstudentov', models.CharField(max_length=100)),
                ('kompensaciya', models.CharField(max_length=100)),
                ('iofrektor', models.CharField(max_length=100)),
                ('dolzn_podrazd', models.CharField(max_length=100)),
                ('iofglavnyi', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OtchetStudenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('this_start', models.CharField(max_length=100)),
                ('fioshort', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prikaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glavbyxfio', models.CharField(max_length=100)),
                ('stringprikaz', models.CharField(max_length=100)),
                ('table_spisokdolznostnixprikaz', models.CharField(max_length=100)),
                ('preambula', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SluzhebnayaZapiska',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podrazdelenie', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Smeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_spisokdolznostnixsmeta', models.CharField(max_length=100)),
                ('rektorfio', models.CharField(max_length=100)),
                ('table_smetastudenta', models.CharField(max_length=100)),
                ('kol_chel', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='common',
        ),
        migrations.DeleteModel(
            name='dva',
        ),
        migrations.DeleteModel(
            name='odin',
        ),
    ]