# sample2.py
# demonstrate a simple view and using Django test client to call it
import django
from django.conf import settings

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='test',
    ALLOWED_HOSTS=['*'],
)

django.setup()

from django.http import HttpResponse
from django.urls import path
from django.test import Client


def home(request):
    return HttpResponse('Hello world')

urlpatterns = [path('', home)]

if __name__ == '__main__':
    client = Client()
    resp = client.get('/')
    print('status', resp.status_code, 'body', resp.content.decode())

