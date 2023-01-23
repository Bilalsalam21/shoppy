# Generated by Django 4.1.5 on 2023-01-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='product',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='user',
        ),
        migrations.RemoveField(
            model_name='products',
            name='images',
        ),
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.DeleteModel(
            name='Carts',
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]