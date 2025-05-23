# Generated by Django 5.2 on 2025-04-30 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filmes', '0002_filmes_delete_filme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avalicoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(choices=[(1, '0'), (2, '1'), (3, '2'), (4, '3'), (5, '4'), (6, '5')])),
                ('comentario', models.TextField(blank=True, null=True)),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='avaliacoes', to='filmes.filmes')),
            ],
        ),
    ]
