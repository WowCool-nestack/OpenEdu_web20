from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),

]