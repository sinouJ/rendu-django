from django.urls import path
from . import views

urlpatterns = [
    path('', views.projets_view, name="projets_view")
]