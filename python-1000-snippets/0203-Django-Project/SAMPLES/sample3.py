# sample3.py
# show how to define a URL pattern and view that accepts POST data
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


def echo(request):
    if request.method == 'POST':
        return HttpResponse(request.POST.get('msg', ''))
    return HttpResponse('send POST')

urlpatterns = [path('echo/', echo)]

if __name__ == '__main__':
    client = Client()
    r1 = client.get('/echo/')
    print('GET ->', r1.status_code, r1.content.decode())
    r2 = client.post('/echo/', {'msg': 'testing'})
    print('POST ->', r2.status_code, r2.content.decode())

