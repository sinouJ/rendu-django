from django.urls import path
from . import views

urlpatterns = [
    path('', views.projets_view, name="projets_view"),
    path('<int:id>/', views.post_view, name='post_view'),
    path('new/', views.post_new, name='post_new'),
    path('<int:id>/edit/', views.post_edit, name="post_edit"),
    path('<int:id>/publish_post/', views.publish_post, name="publish_post"),
    path('<int:id>/archive_post/', views.archive_post, name="archive_post"),
]