# Generated by Django 4.1.3 on 2022-11-28 18:29

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_image', cloudinary.models.CloudinaryField(blank=True, max_length=255)),
            ],
        ),
    ]
