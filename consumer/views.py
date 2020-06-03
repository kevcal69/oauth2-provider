import json

from django.contrib.auth import views, get_user_model
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from oauth2_provider.decorators import protected_resource

from .forms import SignUpForm, LoginForm, UpdateUserForm

User = get_user_model()


class LoginViewAuth(views.LoginView):
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login'
        return context

    def get_success_url(self):
        return reverse_lazy('profile-view', args=(self.request.user.id,))


class RegistrationForm(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['title'] = 'Sign Up'
        return context


class ProfileView(UpdateView):
    model = User
    template_name = 'consumer/profile.html'
    form_class = UpdateUserForm

    def get_success_url(self):
        return reverse_lazy('profile-view', args=(self.request.user.id,))

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return None
        return self.model.objects.filter(id=self.request.user.id)


@protected_resource(scopes=['read'])
def profile(request):
    return HttpResponse(json.dumps({
        "id": request.resource_owner.id,
        "username": request.resource_owner.username,
        "email": request.resource_owner.email,
        "first_name": request.resource_owner.first_name,
        "last_name": request.resource_owner.last_name
    }), content_type="application/json")