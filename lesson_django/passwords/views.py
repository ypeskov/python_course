from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from passwords.models import EncPassword
from users.models import CustomUser


class ListPasswords(LoginRequiredMixin, ListView):
    login_url = 'account_login'
    paginate_by = 50
    template_name = 'passwords/passwords_list.html'
    context_object_name = 'passwords'

    def get_queryset(self):
        return EncPassword.objects.filter(password_user=self.request.user)


class GeneratePasswords(LoginRequiredMixin, TemplateView):
    login_url = 'account_login'

    def get(self, request, *args, **kwargs):
        user = request.user

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


class ClearPasswords(LoginRequiredMixin, TemplateView):
    login_url = 'account_login'

    def get(self, request, *args, **kwargs):
        EncPassword.objects.all().delete()

        return redirect('list_passwords')


class PasswordDetails(LoginRequiredMixin, DetailView):
    login_url = 'account_login'
    model = EncPassword
    template_name = 'passwords/password_details.html'
    context_object_name = 'password'
