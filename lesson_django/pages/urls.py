from django.urls import path

from .views import HomePage, generate


urlpatterns = [
    path('generate', generate, name='generate_passwords'),
]
