from django.urls import path
from .views import RegistrationCreate, registration_success
from django.contrib.auth.decorators import login_required

app_name = 'formula'
urlpatterns = [
    path('', login_required(RegistrationCreate.as_view()), name='add'),
    path('success/', registration_success, name='success'),

]