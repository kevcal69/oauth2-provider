from django.contrib.auth.views import logout_then_login
from django.urls import path
from .views import LoginViewAuth, RegistrationForm, profile, ProfileView


urlpatterns = (
    path('signup/', RegistrationForm.as_view(), name='signup'),
    path('login/', LoginViewAuth.as_view(), name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('profile/view/<int:pk>/', ProfileView.as_view(), name='profile-view'),
    path('profile/', profile, name='profile'),
)
