from django.shortcuts import redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import RegisterForm  
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login


# Create your views here.


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm 
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        user = form.save() # Save the user
        login(self.request, user)
        messages.success(self.request, 'Account created successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error with your submission.')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context



class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('homepage')
    def get_success_url(self):
        return reverse_lazy('homepage')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')
     