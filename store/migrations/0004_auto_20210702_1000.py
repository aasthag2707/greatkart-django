# Generated by Django 3.1 on 2021-07-02 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_reviewrating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewrating',
            old_name='products',
            new_name='product',
        ),
    ]
