from django.urls import path
from u_auth import views

urlpatterns = [
    path('',views.signin,name='sign-in'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('sign-out/',views.signout,name='sign-out')
]