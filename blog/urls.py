from django.urls import path
from blog import views

urlpatterns = [
    urlpatterns = [
    path('', views.index),
    path('<int:pk>', view.single_post_page),
]

