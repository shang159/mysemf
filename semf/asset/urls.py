from .views import list
from django.conf.urls import url
urlpatterns = [
    url('list/', list,name='list'),
    url('', list,name='list'),
]