from django.urls import path
from . import views

app_name = 'meta'

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('signin/', views.signin, name='sign-in'),
    # path('tables/', views.tables, name='tables'),
]



