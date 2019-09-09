from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Create your views here.

def list(request):
    return render(request,"./vuln/list.html")