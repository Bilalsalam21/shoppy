# Generated by Django 4.1.5 on 2023-01-10 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_reviews_product_remove_reviews_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
