from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from web.models import Event, User

from web.forms import EventForm, RegisterForm

def index(request):
  events = Event.objects.all()
  return render(request, 'index.html', {'events': events})

def register(request):
  if request.method == 'POST':
    form = RegisterForm(data=request.POST)
    if form.is_valid():
      user = User.objects.create_user(
        email=form.cleaned_data['email'],
        first_name=form.cleaned_data['first_name'],
        last_name=form.cleaned_data['last_name'],
        password=form.cleaned_data['password']
      )
      user.save()
      return redirect(reverse('index'))

  else:
    form = RegisterForm()
  return render(request, 'registration/register.html', {'form': form})

def create_event(request):
  if request.method == 'POST':
    form = EventForm(data=request.POST)
    if form.is_valid():
      event = form.save()
      event.organiser = request.user
      event.save()
      return redirect(reverse('index'))

  else:
    form = EventForm()

  return render(request, 'create_event.html', {'form': form})
