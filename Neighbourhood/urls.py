
from django.urls import path, include

from Neighbourhood import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('view-post', views.view_post, name='view-post'),
    path('profile', views.profile, name='profile'),

]
