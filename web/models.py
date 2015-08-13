from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
  def create_user(self, email, first_name, last_name, password=None):
    if not email:
      raise ValueError('User must have an email address')
    if not first_name:
      raise ValueError('User must have a first name')
    if not last_name:
      raise ValueError('User must have a last name')

    user = self.model(
        email=UserManager.normalize_email(email),
        first_name=first_name,
        last_name=last_name,
      )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, first_name, last_name, password):
    user = self.create_user(email, first_name, last_name, password=password)
    user.is_admin = True
    user.save(using=self._db)
    return user

class User(AbstractBaseUser):
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)

  is_staff = models.BooleanField(default=False)
  is_admin = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  class Meta:
    ordering = ('created',)

  def get_full_name(self):
    return "%s %s" % (self.first_name, self.last_name)

  def get_short_name(self):
    return "%s" % (self.first_name)

  @property
  def is_superuser(self):
      return self.is_admin

  @property
  def is_staff(self):
      return self.is_admin

  def has_perm(self, perm, obj=None):
    return self.is_admin

  def has_module_perms(self, app_label):
    return self.is_admin

  def __str__(self):
    return "%s %s" % (self.first_name, self.last_name)


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
