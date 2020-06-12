from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logoutUser, name='logout'),
    path('users/', views.users, name='users'),
    path('user/<str:pk_t>/', views.user_update, name="user_update"),
    path('users/<str:pk_t>/delete/', views.user_delete, name="user_delete"),
    path('estimate/', views.estimate, name='estimate'),
    path('result/<str:pk_t>/', views.result, name="result"),
    path('files/', views.files, name='files'),
    path('method/', views.method, name='method'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
