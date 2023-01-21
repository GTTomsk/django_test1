import datetime 

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *


urlpatterns = [
    url(r"^$", login_required(index_view))
]

