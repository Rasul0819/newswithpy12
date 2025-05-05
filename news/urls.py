from django.urls import path
from .views import homepage,detail


urlpatterns =[
    path('',homepage,name='home'),
    path('news/<int:id>/',detail,name='detail'),
]