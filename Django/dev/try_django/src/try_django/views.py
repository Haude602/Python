from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def home_page(request): # we request something to get response on computer
    my_title = "Homepage"
    context = {"title":my_title, "my_list" : [1,2,3,4,5]}
    return render(request,"home.html", context)

def about_page(request): # we request something to get response on computer
    return render(request,"about.html",{"title":"About Us"})

def contact_page(request): # we request something to get response on computer
    return render(request,"contact.html",{"title":"Contact Us"})

def example_page(request): # we request something to get response on computer
    context             = {"title":"Example"}
    template_name       = "hello_world.html"
    template_obj        = get_template(template_name)
    rendered_item       = template_obj.render(context)
    return HttpResponse(rendered_item)