
from django.urls import path, include

from Neighbourhood import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('view-post', views.home, name='view-post'),
    path('post-details', views.home, name='post-details'),

]
