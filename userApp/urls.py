from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login, name='login'),

    url(r'logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
