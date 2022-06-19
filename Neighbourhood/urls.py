
from django.urls import path, include
from django.urls import re_path as url

from Neighbourhood import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('view-post', views.view_post, name='view-post'),
    path('update-profile', views.update_profile, name='profile'),
    path('signup', SignupView.as_view(), name='signup'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('hood-profile', views.hoodProfile, name='hood-profile'),
    path('comment/<id>', views.comment, name='comment'),
    # path('comment', views.comment, name='comment'),


]
