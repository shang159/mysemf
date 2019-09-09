from .views import list,add
from django.conf.urls import url
from django.urls import path
urlpatterns = [
    url("add/", add, name="add"),
    url('', list, name='list'),
    url('list/', list,name='list'),

]