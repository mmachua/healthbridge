

from django.views.generic import TemplateView
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
#from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from login.models import User
#from home.forms import HomeForm, HomeCreate
#from home.models import Post, Friend
#from .models import Create
from home.forms import ContactForm, NewsletterForm
from home.models import Contact, Privacy, Terms, Aboutpage
from login.models import Client, Shop

from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView # new
from django.urls import reverse_lazy
from random import randint
from home.models import Post, Homepage, Aboutpage, Aboutpagee
from django.shortcuts import render, redirect, reverse
from django.conf import settings


import json


@login_required
def home(request):
    return render(request, 'core/home.html')


class HomeView(TemplateView):
    template_name = 'home/home.html'
    model = NewsletterForm
    form_class = NewsletterForm

    def get(self, request):
        form = NewsletterForm()
        posts = Post.objects.all()
        homepages = Homepage.objects.all()

        # Format content
        formatted_content = self.format_homepage_content(homepages.first().content)

        args = {
            'posts': posts, 'homepages': homepages, 'form': form, 'formatted_content': formatted_content
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = NewsletterForm(request.POST)
        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.user = request.user
            newsletter.save()
            title = 'Thanks!!'
            confirm_message = "Thank you for subscribing to our newsletter. Email received."
            context = {'title': title, 'confirm_message': confirm_message }

            return render(request, self.template_name, context)

    def format_homepage_content(self, content):
        # Split the content into lines
        lines = content.split('\n')
        
        # Format the lines
        formatted_lines = []
        for line in lines:
            if line.strip():
                # Check if the line is a section title (ends with ':')
                if line.endswith(':'):
                    formatted_lines.append(f'<strong>{line}</strong>')
                else:
                    # Assume it's a list item without automatic numbering
                    formatted_lines.append(f'<div>{line.strip()}</div>')

        # Combine the lines into an HTML string
        formatted_content = "".join(formatted_lines)
        return formatted_content





class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'home/contact.html'
    success_url = reverse_lazy('shopp:product_list')

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            title = 'Thanks!!'
            confirm_message = 'Thanks for the message. We will get right back to you!'
            context = {'title': title, 'confirm_message': confirm_message}
        return render(request, self.template_name, context)
        #return redirect('shopp:product_list')



class PrivacyView(TemplateView):
    template_name = "home/privacy.html"

    def get(self, request):
        #form = PrivacyForm()
        privacy = Privacy.objects.all()#.order_by('-date')

        args = {'privacy': privacy }
        return render(request, self.template_name, args)

    def post(self, request):
        form = PrivacyForm()
        if form.is_valid():
            #privacy = form.save(commit=False)
            privacy = get_object_or_404(Privacy, id=id, slug=slug)
            privacy.user = request.user
            privacy.save()
            return redirect('home:privacy')
        args = {'privacy':privacy }
        return render(request, self.template_name, args)   


class TermsView(TemplateView):
    template_name = 'home/terms.html'

    def get(self, request):
        terms = Terms.objects.all()
        args = {'terms':terms }
        return render(request, self.template_name, args)

    def post(self, request):
        if form.is_valid():
            terms = get_object_or_404(Terms)
            terms.user = request.user
            terms.user()
            return redirect('home:terms')

        args = {'terms':terms}
        return render(request, self.template_name, args)

class AboutView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aboutpages = Aboutpagee.objects.all()
        context['aboutpages'] = aboutpages
        return context

