from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('privacy/', views.privacy, name="privacy"),
    path('page2/', views.products2, name="products2"),
    path('page3/', views.products3, name="products3")

]
