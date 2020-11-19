from django.shortcuts import render
from django.http import HttpResponse




# Create your views here.
def home_view(request, *args, **kwargs):
    print(*args, **kwargs)
    print(request.user)
    # return HttpResponse("<h1> This is my homepage </h1>") #string with html code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1> This is my Contact page </h1>") #string with html code
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1> This is my About page </h1>") #string with html code
    return render(request, "about.html", {})


def map_view(request, *args, **kwargs):
    return HttpResponse("<h1> This is my map page </h1>") #string with html code
