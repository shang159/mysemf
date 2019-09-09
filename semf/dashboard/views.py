from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
# Create your views here.

def dashboard(request):
    return  render(request,"./dashboard/index.html")