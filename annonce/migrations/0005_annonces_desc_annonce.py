# Generated by Django 3.2.8 on 2022-01-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonce', '0004_annonces_a_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonces',
            name='desc_annonce',
            field=models.TextField(default='pas de description'),
        ),
    ]
