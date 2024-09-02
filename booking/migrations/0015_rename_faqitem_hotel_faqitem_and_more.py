# Generated by Django 5.0.3 on 2024-03-21 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_rename_axis_offer_hotel_axisoffer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FAQItem',
            new_name='hotel_FAQItem',
        ),
        migrations.RenameModel(
            old_name='quary',
            new_name='hotel_quary',
        ),
        migrations.AlterModelTable(
            name='hotel_cards',
            table='cards',
        ),
        migrations.AlterModelTable(
            name='hotel_faqitem',
            table='hotel_FAQItem',
        ),
        migrations.AlterModelTable(
            name='hotel_quary',
            table='quary',
        ),
    ]