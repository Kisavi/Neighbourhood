
from django.urls import path

from Neighbourhood import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('view-post', views.view_post, name='view-post'),
    path('profile', views.profile, name='profile'),
    path('signup', SignupView.as_view(), name='signup')
    path('login')

]
