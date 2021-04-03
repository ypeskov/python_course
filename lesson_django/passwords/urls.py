from django.urls import path

from passwords.views import GeneratePasswords, ClearPasswords, ListPasswords, PasswordDetails


urlpatterns = [
    path('list/', ListPasswords.as_view(), name='list_passwords'),
    path('generate/', GeneratePasswords.as_view(), name='generate_passwords'),
    path('clear/', ClearPasswords.as_view(), name='clear_passwords'),
    path('details/<uuid:pk>', PasswordDetails.as_view(), name='password_details'),
]
