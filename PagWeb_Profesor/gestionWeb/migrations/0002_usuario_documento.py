# Generated by Django 3.2.2 on 2021-07-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionWeb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='documento',
            field=models.IntegerField(null=True),
        ),
    ]