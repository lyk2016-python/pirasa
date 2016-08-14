from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime

from blog.models import Post

def home(request):
	posts = Post.objects.filter(
		is_published=True
	)
	post_count = posts.count()
	return render(request, 'home.html', {
		'name': 'Fatih',
		'posts': posts,
		'post_count': post_count
	})

def post_detail(request, id):
	post = get_object_or_404(Post, id=id)
	return render(request, 'detail.html', {
		'post': post
	})

