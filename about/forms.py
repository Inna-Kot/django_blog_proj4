from django import forms
from .models import NewsletterSubscription

class NewsletterForm(forms.ModelForm):
    """ Form for users to subscribe and provide some details. """
    class Meta:
        model = NewsletterSubscription
        # Adding all fields from the updated model
        fields = ('name', 'email', 'favorite_scent', 'therapy_goal', 'message')
        # Customizing the message field for better UX
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': 'Share any specific candle preferences with us... ...'
            })
        }