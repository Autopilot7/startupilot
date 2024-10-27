# Generated by Django 5.0.2 on 2024-10-27 11:27

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('avatar', models.ImageField(upload_to='avatar/')),
                ('name', models.CharField(blank=True, editable=False, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pitchdeck',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pitchdeck', models.FileField(upload_to='pitchdecks/')),
                ('name', models.CharField(blank=True, editable=False, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('shorthand', models.CharField(blank=True, max_length=200, null=True, unique=True)),
            ],
            options={
                'unique_together': {('name', 'email')},
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('short_description', models.TextField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
                ('phase', models.CharField(blank=True, choices=[('Brainstorming', 'Brainstorming'), ('Fundraising', 'Fundraising'), ('Scaling', 'Scaling'), ('Established', 'Established')], max_length=50, null=True)),
                ('status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=50, null=True)),
                ('priority', models.CharField(blank=True, choices=[('P0', 'P0'), ('P1', 'P1')], max_length=50, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('linkedin_url', models.URLField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='startups', to='startup.avatar')),
                ('batch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='startups', to='startup.batch')),
                ('categories', models.ManyToManyField(blank=True, null=True, related_name='startups', to='startup.category')),
                ('founders', models.ManyToManyField(blank=True, null=True, related_name='startups', to='startup.founder')),
                ('pitch_deck', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='startups', to='startup.pitchdeck')),
            ],
        ),
    ]
