from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.resolvers import URLPattern
from . import views

urlpatterns =[
    path('',views.show,name="frontPage"),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.profile_edit,name='profile-edit'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='ui/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='ui/logout.html'),name='logout'),
]

