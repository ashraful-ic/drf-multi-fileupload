from django.urls import path
from .views import *

urlpatterns = [
    path('', AddCarView.as_view())
]