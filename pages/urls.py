from django.urls import path
from . import views
from django.contrib import admin
from pages import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]