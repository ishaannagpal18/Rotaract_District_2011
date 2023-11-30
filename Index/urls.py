from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about-us',views.about,name='about'),
    path('our-team',views.team,name='team'),
    path('our-projects',views.projects,name='projects'),
    path('gallery',views.gallery,name='gallery'),
    path('user-profile',views.user_profile,name='user_profile'),

]
