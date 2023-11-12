from django.urls import path
from site_forums import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('post/<int:pk>/', views.user_post, name='post'),
    path('create_post/', views.create_post, name='create_post'),
    path('profile/', views.profile, name='profile')
]