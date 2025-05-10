# Django Project

## Description
This snippet demonstrates a Django project with a model, view, template, and URL routing to showcase Django’s ORM and templating features.

## Directory Structure
```
myproject/
├── manage.py
└── myapp/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── models.py
    ├── views.py
    └── templates/
        └── myapp/
            └── index.html
```

## Code
```python
# myapp/models.py
from django.db import models
class Greeting(models.Model):
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

# myapp/views.py
from django.shortcuts import render
from .models import Greeting
def home(request):
    if request.method == "POST":
        message = request.POST.get("message", "Hello")
        Greeting.objects.create(message=message)
    greetings = Greeting.objects.all()
    return render(request, "myapp/index.html", {"greetings": greetings})

# myapp/urls.py
from django.urls import path
from . import views
urlpatterns = [path("", views.home, name="home")]

# myapp/settings.py (partial, ensure INSTALLED_APPS includes 'myapp')
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
]

# Run with `python manage.py migrate` then `python manage.py runserver`
```

```html
<!-- myapp/templates/myapp/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Django Greetings</title>
</head>
<body>
    <h1>Greetings</h1>
    <form method="POST">
        {% csrf_token %}
        <input type="text" name="message" placeholder="Enter a greeting">
        <button type="submit">Add</button>
    </form>
    <ul>
        {% for greeting in greetings %}
            <li>{{ greeting.message }} ({{ greeting.created_at }})</li>
        {% empty %}
            <li>No greetings yet.</li>
        {% endfor %}
    </ul>
    <p><a href="{% url 'home' %}">Home</a></p>
</body>
</html>
```

## Output
```
Mock Output: Django app running at http://127.0.0.1:8000
```
*(Real output with Django: Server runs; visiting `http://127.0.0.1:8000` shows a form and greeting list; submitting a message adds it to the database and updates the list)*

## Explanation
- **Django Project**: Defines a Django app with a `Greeting` model, a view to handle form submissions and queries, and a template to display greetings.
- **Logic**: The `home` view processes POST requests to save greetings and renders `index.html` with all greetings from the database.
- **Complexity**: O(n) for rendering n greetings; O(1) for single-row database operations.
- **Use Case**: Used for building robust web applications with database-backed dynamic content.
- **Best Practice**: Run migrations (`python manage.py makemigrations` and `migrate`); use CSRF tokens; install Django (`pip install django`).