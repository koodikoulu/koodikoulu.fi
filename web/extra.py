from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_signup_confirmation(email_address, guardian, title, organizer):
  email = EmailMessage(
    subject='%s ilmoittautuminen' % title,
    body=render_to_string('mails/signup_confirmation.txt', {'guardian': guardian, 'organizer': organizer}),
    from_email='noreply@koodikoulu.fi',
    to=(email_address,)
  )
  email.send(fail_silently=False)
