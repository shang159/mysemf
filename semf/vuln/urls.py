
from django.conf.urls import url,include
from .views import list,add


urlpatterns = [
    url('add/',add,name='add'),
    url('', list,name='list'),
    url('list/', list,name='list'),

]