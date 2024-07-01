# Generated by Django 5.0.3 on 2024-06-30 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='industries/')),
            ],
        ),
        migrations.CreateModel(
            name='IndustryDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry_image', models.ImageField(blank=True, null=True, upload_to='industries/')),
                ('content', models.TextField()),
                ('key_statistics', models.TextField(blank=True, null=True)),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='industries.industry')),
            ],
        ),
    ]
