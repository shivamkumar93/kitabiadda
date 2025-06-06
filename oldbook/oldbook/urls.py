
from django.contrib import admin
from django.urls import path
from kitab.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("header/",header, name="homepage"),
    path("footer/",footer, name="footerpage"),

]
