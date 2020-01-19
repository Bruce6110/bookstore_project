from django.shortcuts import render
from django.urls import reverse_lazy  #resolves Django URL  names into URL Paths. (occurs within Django framework code)


from django.views import generic

from .forms import CustomUserCreationForm

# Create your views here.

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
