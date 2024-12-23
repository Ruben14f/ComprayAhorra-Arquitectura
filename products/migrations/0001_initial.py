# Generated by Django 5.1.3 on 2024-12-10 19:10

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
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('image', models.ImageField(upload_to='products/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
    ]
