from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('create-note', views.create_note, name='create_note'),
    path('create-ekyc', views.create_ekyc, name='create_ekyc'),
    path('profile', views.profile, name='profile'),
]
