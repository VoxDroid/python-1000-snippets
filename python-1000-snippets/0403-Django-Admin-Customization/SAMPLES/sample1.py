# sample1.py
# Demonstrates configuring Django settings and creating a model table in-memory.

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
    from django.db import models

    if not settings.configured:
        settings.configure(
            INSTALLED_APPS=["django.contrib.contenttypes"],
            DATABASES={
                "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
            },
        )
    django.setup()

    class Example(models.Model):
        name = models.CharField(max_length=100)

        class Meta:
            app_label = "tests"  # required when not in an installed app

        def __str__(self):
            return f"Example(name={self.name})"

    from django.db import connection

    with connection.schema_editor() as editor:
        editor.create_model(Example)

    # Create and query an instance to verify the table exists.
    Example.objects.create(name="Sample")
    print("Created Example:", Example.objects.first())


if __name__ == "__main__":
    main()
