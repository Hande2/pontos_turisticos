# Generated by Django 2.0 on 2019-05-07 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190507_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]