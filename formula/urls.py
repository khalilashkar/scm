from django.urls import path
from . import views
# from .views import RegistrationCreate, registration_success
from django.contrib.auth.decorators import login_required

app_name = 'formula'
urlpatterns = [
    # path('', login_required(RegistrationCreate.as_view()), name='add'),
    path('', views.register_form, name="register_form"),
    # path('success/', registration_success, name='success'),

]
