# Generated by Django 3.0.5 on 2020-04-12 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_pharmacie_pharmacie_ville'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacie',
            name='pharmacie_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
