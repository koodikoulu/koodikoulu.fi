from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from web.forms import EventForm

def index(request):
  return render(request, 'index.html')

def register(request):
  return render(request, 'register.html')

def create_event(request):
  if request.method == 'POST':
    form = EventForm(data=request.POST)
    if form.is_valid():
      event = form.save()
      event.organiser = request.user
      event.save()
      return redirect(reverse('index'))
    else:
      return render(request, 'create_event.html', {'form': form})

  else:
    form = EventForm()

  return render(request, 'create_event.html', {'form': form})
