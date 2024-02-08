from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'aulas', views.AulasViewSet)
urlpatterns = [
    path('', include(router.urls))
]
