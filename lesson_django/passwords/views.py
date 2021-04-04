from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

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


class ClearPasswords(LoginRequiredMixin, View):
    login_url = 'account_login'

    def get(self, request, *args, **kwargs):
        EncPassword.objects.filter(password_user=request.user).delete()

        return redirect('list_passwords')


class PasswordDetails(LoginRequiredMixin, DetailView):
    login_url = 'account_login'
    model = EncPassword
    template_name = 'passwords/password_details.html'
    context_object_name = 'password'

    # def get(self, request, *args, **kwargs):
    #     enc_password = EncPassword.objects.get(id=kwargs['pk'])
    #
    #     if request.user != enc_password.password_user:
    #         return redirect('list_passwords')
    #
    #     return super().get(self, request, args, kwargs)

    def get_context_data(self, **kwargs):
        if self.request.user != kwargs['object'].password_user:
            raise Http404

        context = super().get_context_data(**kwargs)
        context[self.context_object_name] = kwargs['object']

        return context
