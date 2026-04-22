from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('activate/<email_token>/', views.activate_email, name="activate_email"),
    # path('logout/', views.logout, name='logout'),
]