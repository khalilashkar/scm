from django.views.generic.edit import CreateView
from .models import Registration, WorkDetail
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import RegistrationForm, ExperienceForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.forms import formset_factory


# class RegistrationCreate(CreateView):
#     """
#     Affichage du formulaire
#     """
#     model = Registration
#     form_class = RegistrationForm
#     success_url = reverse_lazy('formula:success')


# def registration_success(request):
#     # if request.method == "POST":
#     #     form = RegistrationForm(request.POST)
#     #     if form.is_valid():
#     #         Registration= form.save(commit=False)
#     #         Registration.other = 'khhhhh'
#     #         Registration.save()
#     #         return redirect('formula/registration_success.html')
#     return render(request, 'formula/registration_success.html')

def register_form(request):

    form_register = RegistrationForm(request.POST or None)
    form_experience = formset_factory(ExperienceForm)

    context = {
        'form_register': form_register,
        'form_experience': form_experience,
    }

    return render(request, 'formula/registration_form.html', context)
