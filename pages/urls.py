from django.urls import path
from .views import HomeView, ForumDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<int:pk>/", ForumDetailView.as_view(), name="forum_detail")
]