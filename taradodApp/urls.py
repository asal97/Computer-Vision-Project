from django.urls import path
from .views import *

urlpatterns = [
    path('<int:traffic_id>/', traffic_report, name='traffic_report'),

    # path('', views.register, name='register'),
]
