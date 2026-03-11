# sample1.py
# minimal standalone Django ORM example without creating a full project
import django
from django.conf import settings

# configure Django in standalone script
settings.configure(
    DEBUG=True,
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.auth',
    ],
    DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}},
)
django.setup()

from django.db import models
from django.core.management import call_command

# define a model dynamically
class Greeting(models.Model):
    message = models.CharField(max_length=100)
    class Meta:
        app_label = 'tests'

if __name__ == '__main__':
    # create the table manually using a schema editor
    from django.db import connection
    with connection.schema_editor() as editor:
        editor.create_model(Greeting)
    Greeting.objects.create(message='Hello from Django')
    g = Greeting.objects.first()
    print('Stored message:', g.message)

