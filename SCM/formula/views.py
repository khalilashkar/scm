from django.views.generic.edit import CreateView
from .models import Registration
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

class RegistrationCreate(CreateView):
    """
    Affichage du formulaire
    """
    model = Registration
    form_class = RegistrationForm
    success_url = reverse_lazy('formula:success')

def registration_success(request):
    # if request.method == "POST":
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         Registration= form.save(commit=False)
    #         Registration.other = 'khhhhh'
    #         Registration.save()
    #         return redirect('formula/registration_success.html')
    return render(request, 'formula/registration_success.html')

    
