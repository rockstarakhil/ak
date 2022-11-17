from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	# with auto_now_add=True, the post will automatically be timestamped to whenever the post was created
	# We won't use that param
	date_posted = models.DateTimeField(default=timezone.now)
	# on_delete...: if a user is deleted, then all their posts are deleted as well
	author = models.ForeignKey(User, on_delete=models.CASCADE) 

	def __str__(self):
		"""The “informal” or nicely printable string representation of an object. 
		This is for the end user.
		"""
		return self.title