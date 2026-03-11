# 0203-Django-Project Cheatsheet

* Install Django: `pip install django`.
* Basic structure: `manage.py` and an app directory with `models.py`, `views.py`, `urls.py`, `templates/`.
* Use `django-admin startproject` and `python manage.py startapp` to scaffold.
* Configure `INSTALLED_APPS` and `DATABASES` in `settings.py`.
* Models defined in `models.py`; run `makemigrations` and `migrate` to create tables.
* Views receive `HttpRequest` and return `HttpResponse` or render templates.
* URL routes defined in `urls.py` using `path()` or `re_path()`.
* Templates use the Django templating language; put in `templates/<app>/` or configure `TEMPLATES` setting.
* Run server with `python manage.py runserver` and access via browser.
* Use `django.test.Client` for programmatic requests without running server (see samples).
* In standalone scripts, configure settings manually and call `django.setup()`.
* To create tables without migrations, use:
  ```python
  from django.db import connection
  with connection.schema_editor() as editor:
      editor.create_model(MyModel)
  ```
* Use `call_command('migrate', '--run-syncdb')` for quick table creation when apps listed.
* Use `apps.get_model('app','Model')` to fetch model classes dynamically.
* Best practices: keep apps small, use class-based views for complex logic, protect against CSRF, use the ORM efficiently (select_related, prefetch_related).
