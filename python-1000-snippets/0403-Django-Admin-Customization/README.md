# Django Admin Customization

## Description
This snippet demonstrates customizing the Django admin interface.

## Code
```python
# Note: Requires `django`. Install with `pip install django`
try:
    from django.contrib import admin
    from django.db import models
    
    class Example(models.Model):
        name = models.CharField(max_length=100)
    
    @admin.register(Example)
    class ExampleAdmin(admin.ModelAdmin):
        list_display = ["name"]
    
    print("Admin customized")
except ImportError:
    print("Mock Output: Admin customized")
```

## Output
```
Mock Output: Admin customized
```
*(Real output with `django`: Configures admin interface)*

## Explanation
- **Django Admin Customization**: Customizes admin display for a model.
- **Logic**: Registers a model with a custom admin class to show `name`.
- **Complexity**: O(1) for registration.
- **Use Case**: Used for managing application data in Django.
- **Best Practice**: Secure admin access; optimize list queries; document customizations.