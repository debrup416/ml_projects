from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns =[
    path('',views.getData,name="water-predict"),
    path('result/',views.result,name="result"),
]

