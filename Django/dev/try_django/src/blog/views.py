from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import BlogPost
def blog_post_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    #queryset = BlogPost.objects.filter(slug=slug)
    #if queryset.count() >= 1:
        #obj = queryset.first()
    template_name = "blog_post_detail.html"
    context = {"object":obj}
    return render(request,template_name,context)
