from django import forms
from .models import NewsletterSubscription

class NewsletterForm(forms.ModelForm):
    """
    Form for the NewsletterSubscription model.
    """
    class Meta:
        model = NewsletterSubscription
        fields = ('name', 'email')