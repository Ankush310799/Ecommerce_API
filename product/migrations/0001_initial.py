# Generated by Django 4.2.1 on 2023-05-22 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('images', models.ImageField(blank=True, null=True, upload_to='images')),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('price', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(choices=[('Groccery', 'Groccery'), ('Electronics', 'Electronics'), ('Textile', 'Textile'), ('Health', 'Health'), ('Home_appliences', 'Home_appliences'), ('Footwears', 'Footwears'), ('Toy', 'Toy'), ('Furniture', 'Furniture'), ('other', 'other')], max_length=200, unique=True)),
            ],
        ),
    ]