# Generated by Django 3.1.6 on 2023-09-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliate', '0004_remove_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='img')),
                ('price', models.IntegerField()),
                ('info', models.TextField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]