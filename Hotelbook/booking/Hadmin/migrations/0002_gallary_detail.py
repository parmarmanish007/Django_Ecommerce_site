# Generated by Django 4.0 on 2021-12-14 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm', models.CharField(max_length=100)),
                ('img', models.FileField(upload_to='')),
                ('price', models.IntegerField()),
                ('address', models.TextField()),
                ('area1_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hadmin.area')),
            ],
        ),
    ]
