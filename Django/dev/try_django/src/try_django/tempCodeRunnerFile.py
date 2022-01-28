from django.http import HttpResponse

def home_page(request): # we request something to get response on computer
    return HttpResponse("<h1>HelloWorld<\h1>")