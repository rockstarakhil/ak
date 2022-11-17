from django.shortcuts import render
# Import removed, since we no longer need it
# Kept for posterity
#from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [
	{
	"author":"CoreyMS",
	"title":"Corey's blog post",
	"content":"first post content",
	"date_posted":"12-10-2018"
	},
	{
	"author":"William",
	"title":"William's blog post",
	"content":"second post content",
	"date_posted":"15-10-2018"
	},
]

def home(request):
	"""Return render instance, with input requst, and target template path
	"""
	# Pull data from the database
	context = {'posts':Post.objects.all()}
	return render(request, 'blog/home.html', context)


def about(request):
	about_response = '<h1>About This Throwaway</h>'
	return render(request, 'blog/about.html', {'title':"About"})