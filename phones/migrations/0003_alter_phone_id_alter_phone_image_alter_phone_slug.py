# Generated by Django 5.1.5 on 2025-02-22 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_alter_phone_id_alter_phone_image_alter_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.ImageField(upload_to='phone_images/'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
