
from django.conf.urls import url,include
from .views import list


urlpatterns = [
    url('list/', list,name='list'),
    url('', list,name='list'),
]