
from django.contrib import admin
from django.urls import path
from kitab.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="homepage"),
    path("header/",header, name="headerpage"),
    path("footer/",footer, name="footerpage"),

]
