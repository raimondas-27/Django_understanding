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
    my_context = {
        "title" : "This is about us",
        "this_is_true" : True,
        "my_number" : 123,
        "my_list" : [123,456, 678, "abc"],
        "my_html" : "<h1> Hello world </h1>"

    }

    return render(request, "about.html", my_context)


def map_view(request, *args, **kwargs):
    return HttpResponse("<h1> This is my map page </h1>") #string with html code


def FAQ_view(request, *args, **kwargs):
    # return HttpResponse("<h1> This is my Contact page </h1>") #string with html code
    return render(request, "FAQ.html", {})
