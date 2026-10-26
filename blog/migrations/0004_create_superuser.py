from django.db import migrations


class Migration(migrations.Migration):
    """Superuser is created with `createsuperuser`, not in a migration."""

    dependencies = [
        ('blog', '0003_alter_post_options_comment'),
    ]

    operations = []
