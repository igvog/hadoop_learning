from django.urls import path
from .views import showtime
urlpatterns = [
    path('', showtime),
]