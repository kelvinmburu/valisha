from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('causes/', views.causes, name='causes'),
    path('blog/', views.blog, name='blog'),
    path('contact', views.contact, name='contact')
]