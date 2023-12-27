from django.urls import path

from .views import IndexView, LoginView

urlpatterns = [
    path('', LoginView.as_view()),
]
