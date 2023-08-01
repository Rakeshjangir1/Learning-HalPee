from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('html/', views.html, name='html'),
    path('html/<slug>', views.html_details),
    path('css/', views.css, name='css'),
    path('css/<slug>', views.css_details),
    path('javascript/', views.javascript, name='javascript'),
    path('bootstrap/', views.bootstrap, name='bootstrap'),
    path('python/', views.python, name='python'),

]
