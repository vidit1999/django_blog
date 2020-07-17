from django.conf import settings
from django.urls import path, include
from blog import views

urlpatterns = [
	path('', views.blog_index, name='blog_index'),
	path('<int:blog_id>/', views.blog_view, name='blog_view'),
	path(settings.BLOG_CREATE + '/', views.blog_create, name='blog_create'),
	path(settings.BLOG_CHANGE + '/<int:blog_id>/', views.blog_change, name='blog_change'),
	path(settings.BLOG_DELETE + '/<int:blog_id>/', views.blog_delete, name='blog_delete'),
]