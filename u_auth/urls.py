from django.urls import path
from u_auth import views

urlpatterns = [
    path('',views.signin,name='sign-in'),
]