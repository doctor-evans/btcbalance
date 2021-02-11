from django.urls import path
from . import views


app_name = 'btc'


urlpatterns = [
    path('', views.home, name='home'),
    path('check/', views.check, name='check')
]
