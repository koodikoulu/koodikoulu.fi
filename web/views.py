from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseServerError
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404
from django.utils.encoding import smart_str
from django.conf import settings
from django.utils import timezone

from web.models import Event, User, SignUp, LearningResource, ResourceCategory
from web.forms import EventForm, RegisterForm, LoginForm, SignUpForm
from web.extra import send_signup_confirmation, send_new_event
from datetime import timedelta

import sys
import datetime
import csv
import urllib

def index(request):
  events = Event.objects.filter(approved=True, end_date__gt=datetime.datetime.now() + timedelta(days=-1))
  old_events = Event.objects.filter(approved=True, end_date__lt=datetime.datetime.now() + timedelta(days=-1))
  form = SignUpForm()

  resources = [
    ResourceCategory('Pelien avulla', 'game', [
      LearningResource(
        url = 'http://koodaustunti.fi',
        age = '4 +',
        ageClass = 4,
        languages = 'FI',
        header = 'Tunnin johdatus koodaukseen',
        description = 'Kuka tahansa voi oppia koodauksen perusasiat. Koodaustunti antaa tunnin mittaisen johdatuksen koodaamiseen.',
        free = True),
      LearningResource(
        url = 'http://thefoos.com',
        age = '6 +',
        ageClass = 6,
        languages = 'EN',
        header = 'Opi koodaamista tasohyppelypelissä',
        description = 'The Foos on hauska lapsille suunnattu tasohyppelypeli koodauksen oppimiseen. Pelin saa ladattua mobiililaitteeseen.',
        free = False
      ),
      LearningResource(
        url = 'https://codecombat.com',
        age = '8–16',
        ageClass = 8,
        languages = 'FI/EN',
        header = 'Opi koodaamista seikkailupelissä',
        description = 'Codecombat-pelissä koululainen pääsee opettelemaan koodin kirjoittamista laajasti ja syvällisesti.',
        free = True
      ),
      LearningResource(
        url = 'http://lightbot.com',
        age = '9 +',
        ageClass = 8,
        languages = 'EN',
        header = 'Ratkaise pelissä arvoituksia käyttämällä ohjelmointilogiikkaa',
        description = 'Lightbot-pelissä oppii ohjelmoinnin perusperiaatteita ja ajattelukykyä ohjaamalla robottia.',
        free = True
      )
    ]),
    ResourceCategory('Palikoiden avulla', 'block', [
      LearningResource(
        url = 'https://www.tynker.com',
        age = '7 +',
        ageClass = 6,
        languages = 'EN',
        header = 'Tee pelejä ja ohjelmia visuaalisesti',
        description = 'Tynker-sivustolla on nettikursseja, joissa on interaktiivisia tehtäviä, ohjattua opetusohjelmaa sekä luovia työkaluja koodaamisen opetteluun.',
        free = True
      ),
      LearningResource(
        url = 'https://scratch.mit.edu',
        age = '8–16',
        ageClass = 8,
        languages = 'FI/EN',
        header = 'Luo interaktiivisia pelejä, tarinoita ja animaatioita',
        description = 'Scratch auttaa ajattelemaan luovasti, järkeilemään symmetrisesti ja työskentelemään yhteistyössä.',
        free = True
      )
    ]),
    ResourceCategory('Koodia kirjoittamalla', 'code', [
      LearningResource(
        url = 'http://www.koodikirja.fi',
        age = '4 +',
        ageClass = 6,
        languages = 'FI/EN',
        header = 'Ohjaa kilpikonnaa antamalla käskyjä',
        description = 'Koodikirja on lyhyt web-kirja, jossa opit koodaamaan vekkulin kilpikonnan ja avuliaan robotin kanssa.',
        free = True
      ),
      LearningResource(
        url = 'https://www.codeacademy.com',
        age = '12 +',
        ageClass = 12,
        languages = 'EN',
        header = 'Koodauksen nettiopetus alkeista eteenpäin',
        description = 'CodeAcademy-sivustolta löytyy eri ohjelmointikielten kursseja alkeista lähtien.',
        free = True
      ),
      LearningResource(
        url = 'https://www.khanacademy.org',
        age = '12 +',
        ageClass = 12,
        languages = 'EN',
        header = 'Nettikursseja koodauksen opetteluun',
        description = 'Khan Academy on netissä oleva harjoitteluympäristö, jossa voi opetella koodausta eri ohjelmointikielillä.',
        free = True
      ),
      LearningResource(
        url = 'http://mooc.fi',
        age = '12 +',
        ageClass = 12,
        languages = 'FI/EN',
        header = 'Yliopistotasoisia ohjelmointikursseja',
        description = 'MOOC.FI tarjoaa yliopistotasoisia ohjelmointikursseja kenelle tahansa. Niiden kautta voi jopa hakea opiskelupaikkaa.',
        free = True
      )
    ]),
    ResourceCategory('Lautapelejä pelaamalla', 'boardgame', [
      LearningResource(
        url = 'http://www.robotturtles.com',
        age = '4 +',
        ageClass = 4,
        languages = 'EN',
        header = 'Anna robottikilpikonnalle ohjelmointikäskyjä',
        description = 'Robo turtles -lautapelissä lapsi oppii ohjelmoinnin perusasiat.',
        free = False
      ),
      LearningResource(
        url = 'http://codemonkeyplanet.com',
        age = '5 +',
        ageClass = 4,
        languages = 'EN',
        header = 'Hauska ja mysteerinen ohjelmointia opettava lautapeli',
        description = 'Code monkey island -lautapeli opettaa miten käyttää ja hallita ohjelmoinnin perusteita.',
        free = False
      ),
      LearningResource(
        url = 'http://robogem.fi',
        age = '6 +',
        ageClass = 6,
        languages = 'FI',
        header = 'Ohjelmoi oma robottisi liikkumaan',
        description = 'Robogem-lautapelissä oppii loogista päättelyä sekä hahmottaamaan yksityiskohtaiset ohjelmointikäskyt.',
        free = False
      )
    ]),
    ResourceCategory('Kirjoja lukemalla', 'book', [
      LearningResource(
        url = 'http://www.helloruby.com',
        age = '5–8',
        ageClass = 4,
        languages = 'FI',
        header = 'Tarinamuotoinen lastenkirja ohjelmoinnista',
        description = 'Hello Ruby on Linda Liukkaan kirjoittama koodisatukirja.',
        free = False
      ),
      LearningResource(
        url = 'http://koodi2016.fi',
        age = '18 +',
        ageClass = 18,
        languages = 'FI',
        header = 'Ensiapua ohjelmoinnin opettamiseen peruskouluissa',
        description = 'Koodi2016-opas kertoo, miksi ohjelmointi on tärkeää ja miten sitä voi opettaa.',
        free = True
      )
    ])
  ]

  return render(request, 'index.html', {
    'events': events,
    'old_events': old_events,
    'resources': resources,
    'form': form,
    'key': settings.GOOGLE_KEY,
    'time_now': timezone.now()
  })

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

      return redirect(request.GET.get('next', reverse('organize') + '#create-event'))
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
    if form.is_valid() and request.user.is_authenticated():
      event = form.save(commit=False)
      event.start_time = datetime.time(form.cleaned_data['start_hours'], form.cleaned_data['start_minutes'])
      event.end_time = datetime.time(form.cleaned_data['end_hours'], form.cleaned_data['end_minutes'])

      if form.cleaned_data['signup_open_date']:
        time_string = "%s %s:%s" % (form.cleaned_data['signup_open_date'],
                                    form.cleaned_data['signup_open_hours'],
                                    form.cleaned_data['signup_open_minutes'])
        event.signup_open = datetime.datetime.strptime(time_string, '%Y-%m-%d %H:%M')

      event.organizer = request.user
      event.save()

      # Send a notification to the Slack channel.
      url = "%s/admin/web/event/%d/" % (Site.objects.get_current().domain, event.pk)
      try:
        send_new_event(url)
      except:
        for exc in sys.exc_info():
          print(exc)

      return redirect(reverse('index'))
    else:
      return HttpResponseServerError

  else:
    form = EventForm()

  return render(request, 'organize/organize.html', {
    'create_event_form': form,
    'login_form': LoginForm(),
  })

@csrf_protect
def handle_signup(request, pk):
  if not request.method == 'POST':
    response = HttpResponse('Method not allowed')
    response.status_code = 405
    return response

  event = Event.objects.get(pk=pk)
  if not event:
    return HttpResponseServerError

  if event.booked:
    response = HttpResponse('Tapahtuma on täynnä.')
    response.status_code = 400
    return response

  if event.signup_open and event.signup_open > timezone.now():
    response = HttpResponse('Ilmoittautuminen suljettu.')
    response.status_code = 400
    return response

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

@login_required
def own_events(request):
  events = Event.objects.filter(organizer=request.user)
  return render(request, 'own-events/own-events.html', {
    'events': events,
  })

@csrf_protect
@login_required
def remove_participant(request, pk):
  if not request.method == 'POST':
    response = HttpResponse('Method not allowed')
    response.status_code = 405
    return response

  participant = SignUp.objects.get(pk=pk)
  if not participant:
    return HttpResponseServerError

  if participant.event.organizer != request.user:
    response = HttpResponse('Ei oikeutta poistaa osallistujaa.')
    response.status_code = 403
    return response

  participant.delete()
  return HttpResponse('Osallistuja poistettu')

@login_required
def export_signup_list(request, event_id):
  event = get_object_or_404(Event, pk=event_id)

  if event.organizer != request.user:
    response = HttpResponse('Ei oikeutta ladata tietoja')
    response.status_code = 403
    return response

  response = HttpResponse(content_type='text/csv')
  if is_ascii(event.title):
    title = event.title
  else:
    title = event.title.encode('utf-8')

  if u'WebKit' in request.META['HTTP_USER_AGENT']:
    filename_header = 'filename=%s.csv' % title
  elif u'MSIE' in request.META['HTTP_USER_AGENT']:
    filename_header = ''
  else:
    filename_header = 'filename*=UTF-8\'\'%s' % urllib.quote(title)

  response['Content-Disposition'] = 'attachment; ' + filename_header
  writer = csv.writer(response, csv.excel)
  response.write(u'\ufeff'.encode('utf8'))

  writer.writerow([
    smart_str(u'Nimi'),
    smart_str(u'Huoltajan nimi'),
    smart_str(u'Ikä'),
    smart_str(u'Sähköposti'),
    smart_str(u'Puhelinnumero'),
    smart_str(u'Muuta')
  ])

  for p in event.participants.all():
    writer.writerow([
      smart_str(p.child),
      smart_str(p.guardian),
      smart_str(p.age),
      smart_str(p.email),
      smart_str(p.phone),
      smart_str(p.other)
    ])

  return response

def koodikoulu_404(request):
  return render(request, '404.html')

# Helper function for filenames to check if a string contains only ascii chars
def is_ascii(s):
  return all(ord(c) < 128 for c in s)
