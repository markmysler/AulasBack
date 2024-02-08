from django.urls import path
from .views import MatchingAulasView

urlpatterns = [
    path('get-matching-aulas/', MatchingAulasView.as_view()),
    # Other URL patterns...
]