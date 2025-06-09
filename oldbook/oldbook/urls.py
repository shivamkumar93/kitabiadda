
from django.contrib import admin
from django.urls import path
from kitab.views import *

urlpatterns = [
    #public panel urls
    path('admin/', admin.site.urls),
    path("", home, name="homepage"),
    path("header/",header, name="headerpage"),
    path("footer/",footer, name="footerpage"),

    #user panel urls
    path("login/", login_view, name="loginpage")

    #admin panel urls

]
