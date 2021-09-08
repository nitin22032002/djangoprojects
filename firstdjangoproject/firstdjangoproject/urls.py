"""firstdjangoproject URL Configuration

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
from django.contrib import admin
from django.urls import path,include
import sys
import datetime

from .controllers import Try
from .controllers.client_controllers import auth
test=[
path('admin/', Try.firstResponse),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",include(test)),
    path(f'first/page<int:nums>/name<str:name>',Try.firstResponse,{"name":"nitin"}),
    path(f'second/page<int:nums>/name<str:name>',Try.firstResponse),
]
