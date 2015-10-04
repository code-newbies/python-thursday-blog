#from django.views.generic.base import TemplateView

#class HomeView(TemplateView):
#    template_name = "index.html"

from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

def home(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, "index.html", {})

def about(request):
    return render(request, "about.html", {})

def post(request):
    return render(request, "post.html", {})

def contact(request):
    return render(request, "contact.html", {})
