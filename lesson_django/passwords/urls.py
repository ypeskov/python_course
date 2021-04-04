from django.urls import path

from passwords.views import (
    GeneratePasswords,
    ClearPasswords,
    ListPasswords,
    EncPasswordDetails,
    EncPasswordCreate,
)


urlpatterns = [
    path('list/', ListPasswords.as_view(), name='list_passwords'),
    path('generate/', GeneratePasswords.as_view(), name='generate_passwords'),
    path('clear/', ClearPasswords.as_view(), name='clear_passwords'),
    path('create/', EncPasswordCreate.as_view(), name='create_password'),
    path('details/<uuid:pk>', EncPasswordDetails.as_view(), name='password_details'),
]
