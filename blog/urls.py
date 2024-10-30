from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/', views.post, name='post'),
    path('contact/', views.contact, name='contact'),
    path('article/', views.article, name='article'),
    path('blog_post_detail/<int:post_id>/', views.blog_post_detail, name='blog_post_detail'),
]

if settings.DEBUG:  # Only use this in development, not in production
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)