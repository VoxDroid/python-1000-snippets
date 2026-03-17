# sample3.py
# Demonstrates customizing admin list display and search fields.

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

    class Product(models.Model):
        name = models.CharField(max_length=100)
        price = models.IntegerField()

        class Meta:
            app_label = "tests"

    class ProductAdmin(admin.ModelAdmin):
        list_display = ("name", "price")
        search_fields = ("name",)

    site = admin.AdminSite(name="testadmin")
    site.register(Product, ProductAdmin)

    print("Admin configuration:")
    for model, model_admin in site._registry.items():
        print(f" - {model.__name__}: list_display={model_admin.list_display}, search_fields={model_admin.search_fields}")


if __name__ == "__main__":
    main()
