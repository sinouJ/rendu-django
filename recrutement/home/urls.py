from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="index_view"),
    path('signup/', views.user_signup, name="user_signup"),
    path('logout/', views.user_logout, name="user_logout"),
    path('login/', views.user_login, name="user_login")
]