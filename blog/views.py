from random import sample

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from markdown_it import MarkdownIt

from .models import Articles
from .forms import ArticleForm


# home page
def home(request):
	articles = Articles.objects.all()
	context = {}
	if articles:
		context['articles'] = sample(list(articles),4) if(len(articles) >= 4) else articles
	return render(request, 'blog/blog_home.html', context)

# blog list page
def blog_index(request):
	articles = Articles.objects.all().order_by('-date_modified')
	page_obj = Paginator(articles, 8).get_page(request.GET.get('page'))
	context = {'articles' : articles, 'page_obj' : page_obj}
	return render(request, 'blog/blog_index.html', context)

# blog content page
def blog_view(request, blog_id):
	article = get_object_or_404(Articles, pk=blog_id)
	context = {
		'id' : article.id,	
		'title' : article.title,
		'date_modified' : article.date_modified,
		'article_text' : MarkdownIt().render(article.article_text)
	}
	return render(request, 'blog/blog_text.html', context)


# login page
def blog_login(request):
	if request.user.is_authenticated:
		return redirect(home)

	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(request, username=username, email=email, password=password)

		if user is not None:
			login(request, user)
			return redirect(request.GET['next'] if request.GET.get('next', None) else home)

		else:
			messages.error(request, 'Error : Wrong Credential')

	return render(request, 'blog/blog_login.html', {})

# logout page
def blog_logout(request):
	context = {}
	if request.user.is_authenticated:
		context['username'] = request.user.username
		logout(request)
		return render(request, 'blog/blog_logout.html', context)
	else:
		return redirect(home)

# blog create page
@login_required(login_url = blog_login)
def blog_create(request):
	form = ArticleForm()
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(blog_index)

	return render(request, 'blog/blog_creation.html', {'form' : form})

# change blog
@login_required(login_url = blog_login)
def blog_change(request, blog_id):
	article = get_object_or_404(Articles, pk=blog_id)
	form = ArticleForm(instance = article)

	if request.method == 'POST':
		form = ArticleForm(request.POST, instance = article)
		if form.is_valid():
			form.save()
			return redirect(blog_index)
	return render(request, 'blog/blog_creation.html', {'form' : form})

# delete a blog
@login_required(login_url = blog_login)
def blog_delete(request, blog_id):
	article = get_object_or_404(Articles, pk = blog_id)
	article.delete()
	return redirect(blog_index)

# create user
def create_user(request):
	if request.user.is_authenticated:
		return redirect(home)

	if not User.objects.all():
		if request.method == 'POST':
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password']
			user = User.objects.create_user(username = username, email = email, password = password, is_staff = True, is_superuser = True)
			login(request, authenticate(request, username=username, email=email, password=password))
			return redirect(home)
		else:
			return render(request, 'blog/create_user.html')
	
	return redirect(home)