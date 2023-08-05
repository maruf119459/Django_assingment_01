from django.urls import path
from . import views

urlpatterns = [
  path('show_menu/', views.show_menu),
]