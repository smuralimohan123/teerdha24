# Generated by Django 5.0.6 on 2024-06-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0043_dashboard_sidebar_delete_sidebar'),
    ]

    operations = [
        migrations.CreateModel(
            name='cabs_offerscrud_dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='cabs_secondpage_dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.CharField(max_length=100)),
                ('url_insert', models.URLField()),
                ('offer_data', models.CharField(default='', max_length=100)),
                ('url_update', models.URLField()),
            ],
            options={
                'db_table': 'cabs_secondpage_dashboard',
            },
        ),
    ]
