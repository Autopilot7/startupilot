import uuid
from django.db import models

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Founder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Startup(models.Model):
    PHASE_CHOICES = [
        ('brainstorming', 'Brainstorming'),
        ('fundraising', 'Fundraising'),
        ('scaling', 'Scaling'),
        ('established', 'Established'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=500)
    description = models.TextField()
    phase = models.CharField(max_length=20, choices=PHASE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    contact_email = models.EmailField()
    linkedin_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name="startups")
    founders = models.ManyToManyField(Founder, related_name="startups")
    pitch_deck = models.FileField(upload_to='pitchdecks/')

    def __str__(self):
        return self.name

class StartupCategory(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('startup', 'category')

    def __str__(self):
        return f"{self.startup.name} - {self.category.name}"


class StartupFounder(models.Model):
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    founder = models.ForeignKey(Founder, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('startup', 'founder')

    def __str__(self):
        return f"{self.startup.name} - {self.founder.first_name} {self.founder.last_name}"