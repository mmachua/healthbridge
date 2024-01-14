"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include ,path ,re_path

from login.views import  client , shop, login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls',namespace='home')),
    #path('outreach/',include('outreach.urls',namespace='outreach')),
    path('login/',include('login.urls',namespace='login')),
    path('', include('login.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', login.SignUpView.as_view(), name='signup'),
    path('accounts/signup/client/', client.ClientSignUpView.as_view(), name='client_signup'),
    path('accounts/signup/shop/', shop.ShopSignUpView.as_view(), name='shop_signup'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

