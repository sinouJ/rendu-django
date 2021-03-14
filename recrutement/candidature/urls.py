from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidature_view, name="candidature_view"),
    # path('blabla', views.blabla, name="blabla")
]