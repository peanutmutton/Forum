from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Forum(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="forum_set")
    def __str__(self):
        return self.title

class Thread(models.Model):
    title = models.CharField(max_length=30)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name="thread_set")
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="thread_set")
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="post_set")
    text_content = models.TextField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_set")
    created_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return(self.thread.title + str(self.id))