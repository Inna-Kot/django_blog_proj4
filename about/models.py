from django.db import models

SCENT_CHOICES = (
    ('woody', 'Woody & Earthy'),
    ('floral', 'Floral & Sweet'),
    ('fresh', 'Fresh & Citrus'),
    ('spicy', 'Spicy & Warm'),
)

GOAL_CHOICES = (
    ('stress', 'Stress Relief'),
    ('focus', 'Deep Focus'),
    ('meditation', 'Meditation'),
    ('cozy', 'Cozy Vibe'),
)


class About(models.Model):
    """ Stores a single about me text. """
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class NewsletterSubscription(models.Model):
    """ Model for storing unique newsletter subscriptions."""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    favorite_scent = models.CharField(
        max_length=50, choices=SCENT_CHOICES, default='woody'
    )
    therapy_goal = models.CharField(
        max_length=50, choices=GOAL_CHOICES, default='cozy'
    )
    message = models.TextField(blank=True)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    