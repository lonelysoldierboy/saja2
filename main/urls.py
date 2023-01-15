from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('helper/', views.helper, name='helper'),
    path('victim/', views.victim, name='victim'),
    path('aqhbar/',views.aqhbar,name='aqhbar' ),
]