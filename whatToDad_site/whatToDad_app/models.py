from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(Author, on_delete= models.CASCADE,related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class PostLikes(models.Model):
    user = models.ForeignKey(Author, on_delete= models.CASCADE)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
# Come back to speak about rather we use CASCADE or not

class Activity(models.Model):
    detail = models.CharField(max_length=200, unique=True)
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    addressNumber = models.IntegerField()
    addressStreet = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField()
    user = models.ForeignKey(Author, on_delete= models.CASCADE)

class ActivityComments(models.Model):
    content = models.CharField(max_length=200, unique=True)
    activity = models.ForeignKey(Activity, on_delete= models.CASCADE)

