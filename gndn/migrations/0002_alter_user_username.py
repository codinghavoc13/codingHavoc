# Generated by Django 4.2.7 on 2023-12-26 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gndn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userName',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]