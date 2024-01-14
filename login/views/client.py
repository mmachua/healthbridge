from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator



from login.decorators import client_required
from login.models import  Client, User
from django.views.generic import TemplateView , CreateView
from login.forms import  ClientSignUpForm



from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.contrib.auth import login
from django.urls import reverse_lazy
from smtplib import SMTPAuthenticationError

class ClientSignUpView(CreateView):
    template_name = 'registration/signup_form.html'
    model = Client
    form_class = ClientSignUpForm

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        # Send thank you email to the user
        subject = 'Welcome to CramHub!'
        message = f"Hi {user.first_name},\n\n Discover a new era of Revision!"
        from_email = 'martin@gmail.com'  # Replace with your email
        recipient_list = [user.email]

        try:
            send_mail(subject, message, from_email, recipient_list)
        except SMTPAuthenticationError:
            pass  # Fail silently if email sending fails

        return redirect('bcom:home')

