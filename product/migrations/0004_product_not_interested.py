# Generated by Django 4.2.1 on 2023-05-26 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_per_unit_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='not_interested',
            field=models.BooleanField(default=False),
        ),
    ]
