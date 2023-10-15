from django.contrib import admin
from .models import Category, Forum, Thread


admin.site.register(Category)

admin.site.register(Forum)

admin.site.register(Thread)