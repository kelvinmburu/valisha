from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('update-profile/', views.update_profile, name='update-profile'),
    
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('causes/', views.causes, name='causes'),
    path('blog/', views.blog, name='blog'),
    
    path('paypal', views.paypal, name='paypal'),
    
    path('hood/<str:name>', views.donations, name='hood'),
    path('add_business/', views.add_donation, name='business'),
]