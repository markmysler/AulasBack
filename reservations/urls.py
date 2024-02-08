from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'reservations', views.ReservationViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('my-reservations/<int:pk>/', views.MyReservations.as_view()),
    path('aula-reservations/<int:pk>/', views.AulaReservations.as_view()),
]
