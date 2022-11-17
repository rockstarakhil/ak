# DB Mgmt

To view SQL code generated, run in shell (not in Python shell):

```
python3 manage.py sqlmigrate <app_name> <migration_number>
```

To migrate (i.e. update db):

```
python3 manage.py migrate
```

You'll get the `<migration_number>` from when you run `makemigrate`, or something like that.

## Python Shell

Start python sshell:

```
python3 manage.py shell
```

Sample in-shell commands:

```
# imports
from blog.models.import Post
from django.contrib.auth.models import User

# List all users in a QuerySet object
User.objects.all()

# See first and last user:
User.objects.first()
User.objects.last()

# Filter by a field, and save to a var 'user'
user = User.objects.filter(username="user01").first()

# Some attributes: id, primary key (pk)
user.id
user.pk

# return current Post objects in a QuerySet
Post.objects.all()

# Init new post object
# author defined by user var defined earlier
# This doesn't actually "publish" the post;
# it only exists as a var
post1 = Post(title="Blog Post 1", content="Blog post 1 content", author=user)

# Push to database
post1.save()
```

Interlude: create a dunder method in the Post() object to show more information.

```
# See some post attributes
post.content
post.date_posted # Should return a datetime.datetime object
post.author

# Get all posts by a particular user, in a QuerySet
user.post_set.all()

# Create a post by a particular user
# using .post_set.create() method
# This will automatically be pushed/saved to the DB
user.post_set.create(title="blog3", content="3rd blog content")
```
