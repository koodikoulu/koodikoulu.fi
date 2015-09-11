from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def send_signup_confirmation(email_address, guardian, title, organizer):
  email = EmailMessage(
    subject='%s ilmoittautuminen' % title,
    body=render_to_string('mails/signup_confirmation.txt', {'guardian': guardian, 'organizer': organizer}),
    from_email='noreply@koodikoulu.fi',
    to=(email_address,)
  )
  email.send(fail_silently=False)

def send_new_event(url):
  if not settings.SLACK_CHANNEL_ADDRESS:
    raise NameError('Slack channel not defined')

  email = EmailMessage(
    subject='Koodikoulu new event',
    body=render_to_string('mails/new_event_added.txt', {'url': url}),
    from_email='noreply@koodikoulu.fi',
    to=(settings.SLACK_CHANNEL_ADDRESS,)
  )
  email.send(fail_silently=False)

def send_event_approved(email_address, title, first_name):
  email = EmailMessage(
    subject="%s hyväksytty" % title,
    body=render_to_string('mails/event_approved.txt', {'title': title, 'first_name': first_name}),
    from_email='noreply@koodikoulu.fi',
    to=(email_address,)
  )
  email.send(fail_silently=False)
