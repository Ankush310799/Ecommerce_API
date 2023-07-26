# Generated by Django 4.2.1 on 2023-05-26 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='per_unit',
            field=models.CharField(choices=[('kg', 'kg'), ('gm', 'gm'), ('unit', 'unit'), ('set', 'set')], default='unit', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.CharField(max_length=10),
        ),
    ]
