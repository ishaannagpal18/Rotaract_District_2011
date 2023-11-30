from django.urls import path
from App_Login import views

app_name = 'App_Login'

urlpatterns=[
    path('register-individual/',views.register_individual,name='register_individual'),
    path('login/',views.login_attempt,name='login_attempt'),
    path('logout/',views.logout_user,name='logout'),
    path('register-club/',views.register_club,name='register_club'),

]