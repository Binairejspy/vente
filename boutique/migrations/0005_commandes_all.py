# Generated by Django 4.0 on 2022-02-03 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acceuil', '0011_alter_clients_emailclient_and_more'),
        ('boutique', '0004_commandes'),
    ]

    operations = [
        migrations.CreateModel(
            name='commandes_all',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomproduitcommande_all', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boutique.article', verbose_name='le produit commander')),
                ('nomusercommande_all', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acceuil.clients', verbose_name='le commandeur')),
            ],
        ),
    ]
