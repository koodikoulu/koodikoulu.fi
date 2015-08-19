from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout

from web.models import Event, User, SignUp
from web.forms import EventForm, RegisterForm, LoginForm, SignUpForm

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

      return redirect(reverse('index'))

  else:
    form = RegisterForm()
  return render(request, 'registration/register.html', {'form': form})

def login_view(request):
  if request.user.is_authenticated():
    return redirect(reverse('index'))

  if request.method == 'POST':
    form = LoginForm(data=request.POST)
    if form.is_valid():
      user = form.login(request)
      if user:
        login(request, user)
        return redirect(reverse('index'))

  else:
    form = LoginForm()
  return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
  logout(request)
  return redirect(reverse('index'))

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

def handle_signup(request, pk):
  if not request.method == 'POST':
    return JsonResponse({'status': 405})

  event = Event.objects.get(pk=pk)
  if not event:
    return JsonResponse({'status': 500})

  form = SignUpForm(data=request.POST)
  if form.is_valid():
    signup = SignUp.objects.create(event=event, **form.cleaned_data)
    return JsonResponse({'status': 200})
  else:
    return JsonResponse({'status': 500})
