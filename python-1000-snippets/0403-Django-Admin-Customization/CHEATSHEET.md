# 0403-Django-Admin-Customization Cheatsheet

- Use `django.conf.settings.configure()` to set up minimal settings for standalone scripts.
- Call `django.setup()` after configuring settings.
- Register models with `admin.site.register(Model, ModelAdmin)` to customize the admin interface.
- Customize list display columns via `list_display` and searchable fields via `search_fields`.
- Use `django.db.connection.schema_editor()` to create model tables without running migrations.
