from .views import dashboard
from django.conf.urls import url
urlpatterns = [
    url('index/', dashboard,name='dashboard'),
    url('', dashboard,name='dashboard'),
]