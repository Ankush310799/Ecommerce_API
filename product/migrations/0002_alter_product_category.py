# Generated by Django 4.2.1 on 2023-05-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Groccery', 'Groccery'), ('Electronics', 'Electronics'), ('Textile', 'Textile'), ('Health', 'Health'), ('Home_appliences', 'Home_appliences'), ('Footwears', 'Footwears'), ('Toy', 'Toy'), ('Furniture', 'Furniture'), ('other', 'other')], max_length=200),
        ),
    ]
