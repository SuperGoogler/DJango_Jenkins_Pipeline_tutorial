from django.urls import path
from .views import home, login_user, logout_user, register_user, userprofileview, profile_page, contact, thank_you, about

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path("login/", login_user, name='login'),
    path("logout/", logout_user, name='logout'),
    path("register/", register_user, name='register'),
    path("bolo/", userprofileview, name='bolo'),
    path('profile1/', profile_page, name='profile1'),
    path('thank_you/', thank_you, name='thank_you'),
    path('about/', about, name='about'),
]
