from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views import View
from django.shortcuts import redirect
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.forms import PasswordChangeForm

def send_transaction_email(user, subject, template):
    message = render_to_string(template, {'user' : user,})
    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()


class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('homepage')
    
    def form_valid(self,form):
        # print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        # print(user)
        send_transaction_email(user, 'Welcome to Our Site', 'accounts/welcome_email.html')
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('homepage')


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'
    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, self.template_name, {'form': form})

# nurmohammadimon19@gmail.com

@method_decorator(login_required, name='dispatch')
class PasswordChangeView(PasswordChangeView):
    template_name = 'accounts/pass_change.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request, 'Password Changed Successfully')
        update_session_auth_hash(self.request, form.user)
        send_transaction_email(form.user, 'Password Changed Successfully', 'accounts/pass_change_email.html')
        return super().form_valid(form)