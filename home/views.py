from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")


def homepage(request):
    return HttpResponse("Hello, world. You're at the home index.")