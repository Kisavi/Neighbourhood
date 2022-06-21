
from django.urls import path, include
from django.urls import re_path as url

from Neighbourhood import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('update-profile', views.update_profile, name='profile'),
    path('signup', SignupView.as_view(), name='signup'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('hood-profile', views.hoodProfile, name='hood-profile'),
    path('comment/<id>', views.comment, name='comment'),
    path('search', SearchBusinessView.as_view(), name='search_business'),
    path('welcome', views.welcome, name='welcome'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    # path('alerts', views.alert, name='alerts'),
    # path('posts', views.post, name='posts'),
    # path('business', views.business, name='business'),



]
