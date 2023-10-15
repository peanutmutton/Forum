from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import FormView
from .models import Category, Forum, Thread, Post
from .forms import PostForm
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.views.generic.detail import SingleObjectMixin
from django.views import View

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

class ThreadDetailView(DetailView):
    model = Thread
    template_name = "thread_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["forum_pk"] = self.object.forum.pk
        context["form"]=PostForm
        return context

class ThreadFormView(SingleObjectMixin, FormView):
    template_name = "thread_detail.html"
    form_class = PostForm
    model = Thread

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("thread_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        post = Post.objects.create(
            text_content = form.cleaned_data['text_field'],
            poster = self.request.user,
            thread=self.object
        )
        return super().form_valid(form)


class ThreadView(View):
    def get(self, request, *args, **kwargs):
        view = ThreadDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ThreadFormView.as_view()
        return view(request, *args, **kwargs)
