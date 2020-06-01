from django.contrib.auth import views
from .forms import SignUpForm, LoginForm


class LoginViewAuth(views.LoginView):
    form_class = LoginForm


class RegistrationForm(views.FormView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'