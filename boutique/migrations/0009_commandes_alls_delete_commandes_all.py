# Generated by Django 4.0 on 2022-01-14 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acceuil', '0011_alter_clients_emailclient_and_more'),
        ('boutique', '0008_commandes_all_delete_commandes_alls'),
    ]

    operations = [
        migrations.CreateModel(
            name='commandes_alls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_produit', models.IntegerField()),
                ('nomusercommande_all', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acceuil.clients')),
            ],
        ),
        migrations.DeleteModel(
            name='commandes_all',
        ),
    ]
