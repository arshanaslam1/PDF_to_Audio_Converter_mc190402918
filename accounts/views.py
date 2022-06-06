from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as gen_views
from .forms import AccountRegisterForm, AccountLoginForm

class AccountRegisterView(gen_views.CreateView):
    form_class = AccountRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
    success_message = 'you have register you account successfully'


class AccountLoginView(auth_views.LoginView):
    authentication_form = AccountLoginForm
    form_class = AccountLoginForm
    template_name = 'accounts/login.html'


class AccountLogoutView(auth_views.LogoutView):
    pass


