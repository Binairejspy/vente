# Generated by Django 4.0 on 2022-03-10 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceuil', '0012_commenteur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelances',
            name='prix_jours',
            field=models.CharField(max_length=255),
        ),
    ]
