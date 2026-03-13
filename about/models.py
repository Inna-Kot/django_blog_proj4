from django.db import models

class About(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class NewsletterSubscription(models.Model):
    """
    Model for storing unique newsletter subscriptions.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"