from django.contrib import admin
from .models import NewsletterSubscription

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the NewsletterSubscription model.
    """
    list_display = ('name', 'email', 'subscribed_on')
    search_fields = ('name', 'email')
    list_filter = ('subscribed_on',)