from . import views
from django.urls import path


urlpatterns = [
    path('', views.main.as_view(), name='first-page'),
    path('input/', views.inputPage.as_view(), name='input')
]