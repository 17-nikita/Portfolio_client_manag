# website/admin.py

from django.contrib import admin
from .models import Project, Client, ContactSubmission, NewsletterSubscription

admin.site.register(Project)
admin.site.register(Client)
admin.site.register(ContactSubmission)
admin.site.register(NewsletterSubscription)