from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    is_published = models.BooleanField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    name = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments")
    
    def __str__(self):
        return self.body
