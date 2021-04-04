# Generated by Django 2.2.10 on 2021-04-04 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TBL_DEVICE_INFO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('station', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('install_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TBL_TOTAL_INFO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.IntegerField()),
                ('total_pop', models.IntegerField()),
                ('mask_pop', models.IntegerField()),
                ('high_temp_pop', models.IntegerField()),
                ('region', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TBL_PERSON_INFO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.FloatField()),
                ('has_mask', models.BooleanField()),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TBL_DEVICE_INFO')),
            ],
        ),
    ]
