# Generated by Django 3.1.1 on 2020-09-20 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/category_img'),
        ),
        migrations.AlterField(
            model_name='food',
            name='secondary_image_1',
            field=models.ImageField(blank=True, upload_to='images/food_image'),
        ),
        migrations.AlterField(
            model_name='food',
            name='secondary_image_2',
            field=models.ImageField(blank=True, upload_to='images/food_image'),
        ),
        migrations.AlterField(
            model_name='food',
            name='secondary_image_3',
            field=models.ImageField(blank=True, upload_to='images/food_image'),
        ),
    ]
