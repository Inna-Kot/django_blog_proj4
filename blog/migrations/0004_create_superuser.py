from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='inna_kot').exists():
        User.objects.create(
            username='admin',
            password=make_password('temfamily'),
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options_comment'),  
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
