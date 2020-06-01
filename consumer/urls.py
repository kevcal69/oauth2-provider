from django.urls import path
from .views import LoginViewAuth, RegistrationForm


urlpatterns = (
    path('signup/', RegistrationForm.as_view()),
    path('login/', LoginViewAuth.as_view()),
)
