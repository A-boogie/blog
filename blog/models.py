from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()


# to display the title field of any blog post
def __str__(self):
    return self.title
