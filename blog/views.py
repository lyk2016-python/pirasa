from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect

from blog.models import Post, Comment
from blog.forms import CommentForm

def home(request):
	posts = Post.objects.filter(
		is_published=True
	)
	post_count = posts.count()
	return render(request, 'home.html', {
		'posts': posts,
		'post_count': post_count
	})

def post_detail(request, id):
	post = get_object_or_404(Post, id=id)
	comments = post.comments.all()

	form = CommentForm()

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.instance.post_id = id
			form.save()
			return redirect('/posts/%s' %id)

	return render(request, 'detail.html', {
		'post': post,
		'comments': comments,
		'form': form,
	})


