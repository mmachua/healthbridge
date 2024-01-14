from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from django.http import Http404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
#from django.contrib.auth.forms import RegistrationForm
#from login.forms import ( EditProfileForm)
#from django.contrib.auth.models import User
from ..models import User
#from shopp.models import ResidentAddress
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm#, EditProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from login.forms import  EditProfileForm#, contactForm
#from home.views import Post

from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
#
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template


from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.conf import settings

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

    def signup(self, request):
        if request.method == 'POST':
            # Process signup form data here
            
            # Send welcome email to the user
            user_email = request.POST['email']  # Assuming email is submitted in the signup form
            send_mail(
                'Welcome to My Website',  # Subject of the email
                'Thank you for signing up to My Website!',  # Message of the email
                settings.DEFAULT_FROM_EMAIL,  # From email address
                [user_email],  # To email address (recipient)
                fail_silently=False,  # Raise exceptions for errors
            )
            
            # Redirect to desired view after signup
            if request.user.is_authenticated:
                if request.user.is_shop:
                    return redirect('bcom:home')
                elif request.user.is_client:
                    return redirect('bcom:home')
                else:
                    return redirect('bcom:home')
            else:
                # Return an appropriate response for non-authenticated users
                return render(request, 'bcom:home')
        else:
            # Return an appropriate response for non-POST requests
            return render(request, self.template_name)


# class SignUpView(TemplateView):
#     template_name = 'registration/signup.html'

#     def home(self, request):
#         if request.user.is_authenticated:
#             if request.user.is_shop:
#                 return redirect('shopp:residentadressform')
#             else:

            
#                 return redirect('shopp:residentadressform')
#             if request.user.is_client:

#                 return redirect('shopp:residentadressform')
            
#             else:
#                 return redirect('shopp:residentadressform')
        
#         return render(request,'shopp:residentadressform')

#    def get(self, request):
#        if request.user.is_authenticated:
#            if request.user.is_client:
##                return redirect('shopp:product_list')
 #           else:
#                return redirect('shopp:product_list')
#        return render(request,'registration/signup.html')






@login_required
def login_admin(request):
    return render(request, 'admin/login.html')


