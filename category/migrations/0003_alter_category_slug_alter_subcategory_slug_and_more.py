# Generated by Django 4.0.5 on 2024-01-25 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_slug_subcategory_slug_subsubcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='subsubcategory',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
