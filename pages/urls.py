from django.urls import path
from .views import HomeView, ForumDetailView, ThreadDetailView, ThreadView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    path("<int:forum_pk>/<int:pk>/", ThreadView.as_view(), name="thread_detail"),
    path("<int:pk>/", ForumDetailView.as_view(), name="forum_detail"),
]