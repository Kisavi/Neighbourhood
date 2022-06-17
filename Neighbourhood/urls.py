
from django.urls import path, include
from django.urls import re_path as url

from Neighbourhood import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('view-post', views.view_post, name='view-post'),
    path('profile', views.profile, name='profile'),
    path('signup', SignupView.as_view(), name='signup'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),


]
