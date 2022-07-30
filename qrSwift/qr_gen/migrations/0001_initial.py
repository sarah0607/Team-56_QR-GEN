# Generated by Django 4.0.6 on 2022-07-29 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='qr_gen',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=200)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes')),
            ],
        ),
    ]