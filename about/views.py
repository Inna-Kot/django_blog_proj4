from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import NewsletterForm


def about_me(request):
    """Renders the About page and handles newsletter subscriptions."""
    if request.method == "POST":
        newsletter_form = NewsletterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Success! You are now subscribed to our cozy newsletter."
            )
            newsletter_form = NewsletterForm()
    else:
        newsletter_form = NewsletterForm()

    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "newsletter_form": newsletter_form
        },
    )
