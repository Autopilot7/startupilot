# Generated by Django 5.0.2 on 2024-10-25 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0003_founder_shorthand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founder',
            name='shorthand',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
