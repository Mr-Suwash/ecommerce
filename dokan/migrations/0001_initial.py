# Generated by Django 5.0.6 on 2024-08-14 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, verbose_name='')),
                ('Price', models.FloatField(verbose_name='')),
                ('Discount', models.FloatField(verbose_name='')),
                ('Description', models.TextField(verbose_name='')),
            ],
        ),
    ]
