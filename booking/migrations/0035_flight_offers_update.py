# Generated by Django 5.0.3 on 2024-06-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0034_flightfaqs_delete_faqs_alter_hotel_faqitem_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='flight_offers_update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offers', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
    ]
