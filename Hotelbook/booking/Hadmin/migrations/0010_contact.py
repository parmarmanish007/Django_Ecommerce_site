# Generated by Django 4.0 on 2021-12-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hadmin', '0009_alter_wishlist_detail_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]
