# Generated by Django 4.2.4 on 2023-11-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('med_name', models.CharField(max_length=255)),
                ('usage', models.CharField(max_length=255)),
                ('qty', models.IntegerField()),
            ],
        ),
    ]
