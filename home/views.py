from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the home index.")


def homepage(request):
    return HttpResponse("Hello, world. You're at the home index.")