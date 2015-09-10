from django.shortcuts import render
from blog.models import Post

# Create your views here.
def list_posts(request):
	posts = Post.objects.all()
	title = 'Python Thursday Blog - Posts'
	return render(request, 'posts.html', {'posts': posts, 'title': title})
