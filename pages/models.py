from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30)

class Forum(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="forum_set")

class Thread(models.Model):
    title = models.CharField(max_length=30)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name="thread_set")

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    text_content = models.TextField()
