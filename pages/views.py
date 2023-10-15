from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Category, Forum

class HomeView(ListView):
    model = Category
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context["something"] = something
        return context

class ForumDetailView(DetailView):
    model = Forum
    template_name = "forum_detail.html"