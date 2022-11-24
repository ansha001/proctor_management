from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import activate  

urlpatterns = [
    path('', views.facultyhome, name='faculty-home'),
    path('login/', auth_views.LoginView.as_view(template_name= 'faculty/login.html'), name='faculty-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'faculty/logout.html'), name='faculty-logout'),
    path('register/', views.facultyregister, name='faculty-register'),
    path('profile/', views.profile, name='faculty-profile'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name= 'faculty/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'faculty/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'faculty/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'faculty/password_reset_complete.html'), name='password_reset_complete'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate, name='activate')

]

