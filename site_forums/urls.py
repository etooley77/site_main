from django.urls import path, include
from site_forums import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('post/<int:pk>/', views.user_post, name='post'),
    path('create_post/', views.create_post, name='create_post'),
    path('profile/', views.profile, name='profile'),

    path('music/', views.music, name='music'),
    path('upload_music/', views.upload_music, name='upload_music'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)