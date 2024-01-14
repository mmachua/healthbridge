from django.conf.urls import url
from django.urls import include, re_path

from django.contrib.auth import views as auth_views

from home import views
from . import views 
from home.views import ContactView, PrivacyView, TermsView,  AboutView, HomeView

app_name = 'home'


urlpatterns = [
    re_path(r'^$', HomeView.as_view(), name='home'),
    re_path(r'^privacy/', PrivacyView.as_view(), name='privacy' ),
    re_path(r'^terms/', TermsView.as_view(), name='terms'),
    re_path('contact/', ContactView.as_view(), name='Contact'),
    re_path(r'^about/', AboutView.as_view(), name='about'),

  
]


