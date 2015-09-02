from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseServerError
from django.contrib.auth import authenticate, login, logout

from web.models import Event, User, SignUp
from web.forms import EventForm, RegisterForm, LoginForm, SignUpForm
from web.extra import send_signup_confirmation

import sys

def index(request):
  events = Event.objects.all()
  form = SignUpForm()
  return render(request, 'index.html', {'events': events, 'form': form})

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
      user.backend = 'django.contrib.auth.backends.ModelBackend'
      user.save()
      login(request, user)

      return redirect(request.GET.get('next', reverse('index')))
  else:
    form = RegisterForm()

  return render(request, 'registration/register.html', {'form': form})

def login_view(request):
  next_page = reverse('organize') # Hard-coded for now

  if request.user.is_authenticated():
    return redirect(next_page)

  if request.method == 'POST':
    form = LoginForm(data=request.POST)
    if form.is_valid():
      user = form.login(request)
      if user:
        login(request, user)
        return redirect(next_page + '#create-event')
  else:
    form = LoginForm()

  return render(request, 'organize/organize.html', {
    'login_form': form,
    'create_event_form': EventForm(),
  })

def logout_view(request):
  logout(request)
  return redirect(reverse('index'))

def organize(request):
  if request.method == 'POST':
    form = EventForm(data=request.POST)
    if form.is_valid():
      event = form.save()
      event.time = "%d:%d-%d:%d" % (
        form.cleaned_data['start_hours'],
        form.cleaned_data['start_minutes'],
        form.cleaned_data['end_hours'],
        form.cleaned_data['end_minutes']
      )
      event.organizer = request.user
      event.save()
      return redirect(reverse('index'))

  else:
    form = EventForm()

  return render(request, 'organize/organize.html', {
    'create_event_form': form,
    'login_form': LoginForm(),
  })

def handle_signup(request, pk):
  if not request.method == 'POST':
    response = HttpResponse('Method not allowed')
    response.status_code = 405
    return response

  event = Event.objects.get(pk=pk)
  if not event:
    return HttpResponseServerError

  form = SignUpForm(data=request.POST)
  if form.is_valid():
    signup = SignUp.objects.create(event=event, **form.cleaned_data)
    try:
      send_signup_confirmation(signup.email, signup.guardian, event.title, event.organizer)
    except:
      for exc in sys.exc_info():
        print(exc)

    return HttpResponse('Kiitos ilmoittautumisesta!')
  else:
    return HttpResponseServerError

def story(request):
  return render(request, 'story.html')