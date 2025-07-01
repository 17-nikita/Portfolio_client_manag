from django.db import models


class Project(models.Model):
    image = models.ImageField(upload_to='projects/') # Images will be stored in MEDIA_ROOT/projects/
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

   

class Client(models.Model):
    image = models.ImageField(upload_to='clients/') # Images will be stored in MEDIA_ROOT/clients/
    name = models.CharField(max_length=255)
    description = models.TextField()
    designation = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ContactSubmission(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.full_name}"

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email