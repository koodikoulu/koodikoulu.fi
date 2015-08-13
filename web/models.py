from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)
  start_date = models.DateField()
  end_date = models.DateField(blank=True, null=True)
  street_address = models.CharField(max_length=100)
  city = models.CharField(max_length=40)
  amount = models.PositiveIntegerField()
  created = models.DateTimeField(auto_now_add=True)
  booked = models.BooleanField(default=False)

  organizer = models.ForeignKey(User, blank=True, null=True, related_name="events")

  class Meta:
    ordering = ('start_date',)

  def __str__(self):
    return "%s" % self.title

class SignUp(models.Model):
  child = models.CharField(max_length=100)
  guardian = models.CharField(max_length=100)
  age = models.PositiveIntegerField()
  email = models.EmailField()
  phone = models.CharField(max_length=100, blank=True, null=True)
  other = models.TextField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)

  event = models.ForeignKey(Event, related_name="participants")

  class Meta:
    ordering = ('created',)

  def save(self, *args, **kwargs):
    super(SignUp, self).save(*args, **kwargs)
    if (len(self.event.participants) + 1) >= self.event.amount:
      self.event.booked = True
      self.event.save()

  def __str__(self):
    return "%s" % self.child
