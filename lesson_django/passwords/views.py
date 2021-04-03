from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView

from passwords.models import EncPassword
from users.models import CustomUser


class ListPasswords(ListView):
    model = EncPassword
    paginate_by = 10
    template_name = 'passwords/passwords_list.html'
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

        return render(request, 'passwords/generate_passwords.html', context=context)


class ClearPasswords(TemplateView):
    def get(self, request, *args, **kwargs):
        EncPassword.objects.all().delete()

        return redirect('list_passwords')


class PasswordDetails(DetailView):
    model = EncPassword
    template_name = 'passwords/password_details.html'
    context_object_name = 'password'
