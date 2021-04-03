
from django.views.generic import TemplateView

from users.models import CustomUser
from passwords.models import EncPassword


class HomePage(TemplateView):
    template_name = 'pages/home.html'



