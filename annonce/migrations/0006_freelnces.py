# Generated by Django 4.0 on 2022-01-14 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acceuil', '0003_clients_numero'),
        ('annonce', '0005_annonces_desc_annonce'),
    ]

    operations = [
        migrations.CreateModel(
            name='freelnces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualite', models.CharField(max_length=200)),
                ('biographie', models.TextField()),
                ('prix_jours', models.IntegerField()),
                ('nomfree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acceuil.clients')),
            ],
        ),
    ]
