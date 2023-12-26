from django.urls import path

from .views import CurrentDateView, RandomView, HelloView, IndexView, current

urlpatterns = [
    path('datetime/', CurrentDateView.as_view()),
    path('random/', RandomView.as_view()),
    path('hello/', HelloView.as_view()),
    path('index/', IndexView.as_view()),
    path('func/', current), # функциональный метод
]
