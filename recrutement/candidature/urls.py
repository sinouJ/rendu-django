from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.candidature_view, name="candidature_view"),
    path('postcv/', views.post_cv_view, name="post_cv_view"),
    path('detail_candidature/<int:id>/', views.detail_candidature_view, name="detail_candidature_view")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)