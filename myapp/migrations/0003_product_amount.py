# Generated by Django 3.1.5 on 2021-01-30 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(max_length=500, null=True),
        ),
    ]