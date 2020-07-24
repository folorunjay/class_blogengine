from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('post_detail/<slug:slug>/', views.post_detail,name='postdetail'),
    path('register/', views.register,name='register'),
    path('createpost/', views.createpost,name='createpost'),
]