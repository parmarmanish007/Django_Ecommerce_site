# Generated by Django 4.0 on 2021-12-22 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hadmin', '0008_alter_booking_detail2_id_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='detail_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hadmin.detail'),
        ),
    ]
