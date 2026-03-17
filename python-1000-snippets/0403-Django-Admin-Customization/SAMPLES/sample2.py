# sample2.py
# Demonstrates registering a model with the Django admin site programmatically.

import subprocess
import sys


def ensure_django():
    try:
        import django  # type: ignore
        return django
    except ImportError:
        print("Missing dependency: django. Install with: python -m pip install django")
        sys.exit(1)


def main() -> None:
    django = ensure_django()

    from django.conf import settings
    from django.contrib import admin
    from django.db import models

    if not settings.configured:
        settings.configure(
            INSTALLED_APPS=["django.contrib.contenttypes", "django.contrib.auth"],
            DATABASES={
                "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
            },
        )
    django.setup()

    class Example(models.Model):
        name = models.CharField(max_length=100)

        class Meta:
            app_label = "tests"

    class ExampleAdmin(admin.ModelAdmin):
        list_display = ("id", "name")

    site = admin.AdminSite(name="testadmin")
    site.register(Example, ExampleAdmin)

    # Show registered models for the site
    print("Registered models:")
    for model, model_admin in site._registry.items():
        print(f" - {model.__name__} (admin: {type(model_admin).__name__})")


if __name__ == "__main__":
    main()
