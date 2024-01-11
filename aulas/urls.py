from django.urls import path, include
from aulas import views

urlpatterns = [
    path('get-aulas/', views.AulasList.as_view()),
]