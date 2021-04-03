from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from passwords.models import EncPassword
from users.models import CustomUser


class ListPasswords(ListView):
    model = EncPassword
    template_name = 'passwords/list.html'
    context_object_name = 'passwords'


class GeneratePasswords(TemplateView):
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.get(username='admin')

        passwords = []
        for i in range(30):
            passwords.append(
                EncPassword(name='resource-' + str(i),
                            password_user=user,
                            encrypted_password='XXX-' + str(i),
                            username='user-' + str(i),
                            url='http://google.com')
            )

        EncPassword.objects.bulk_create(passwords)

        context = {
            'passwords': passwords
        }

        return render(request, 'pages/create_passwords.html', context=context)


class ClearPasswords(TemplateView):
    def get(self, request, *args, **kwargs):
        passwords = EncPassword.objects.all().delete()

        return redirect('list_passwords')

