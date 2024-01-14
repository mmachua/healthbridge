
from django.urls import include, path
from .views import login, client, shop
from django.conf import settings
from django.conf.urls import url
from django.urls import include, re_path
from django.urls import include ,path
from django.contrib.auth import (
    login,
    logout,
#     password_reset_confirm,
#      password_reset,
#     password_reset_done,
#     password_reset_complete
     )
from django.contrib.auth.views import(
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from . import views as myapp_views
from . import views
from  .views import login 

app_name = 'login'

urlpatterns = [

    path('clients/', include(([
       

        #re_path(r'^delete/(?P<username>[\w|\W.-]+)/$', views.delete_user, name='delete-user')

    ]))),


    path('shops/', include(([
        #re_path(r'^profile/$',login.ProfileView.as_view(), name='profile'),
        

    ])))
 
]




    