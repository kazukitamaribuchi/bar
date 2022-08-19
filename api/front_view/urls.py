from django.urls import path
from . import views

app_name = 'front_view'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<path:path>', views.HomeView.as_view(), name='sub_home'),
]
