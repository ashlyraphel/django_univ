from django.conf.urls import include, url
from register.views import *
from register.models import *
from register.views import UserRegistrationView


urlpatterns = [
    url(r'^signup/$', UserRegistrationView.as_view(), name='signup'),
]