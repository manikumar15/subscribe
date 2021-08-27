
from django.contrib import admin
from django.urls import path
from subscribeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.newsletter2)
]
