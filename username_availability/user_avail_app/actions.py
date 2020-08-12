from django.shortcuts import redirect, render
from .models import User
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        User.objects.create(
            username = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password']
        )
        return redirect('/')

def username(request):
    context = {
        'found': False
    }
    if len(User.objects.filter(username=request.POST['username'])) > 0:
        context['found'] = True
    return render(request, 'partials/name_unavailable.html', context)
