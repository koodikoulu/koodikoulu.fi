from django import forms, template
from web.models import Event, SignUp
from django.contrib.auth import authenticate

class EventForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(EventForm, self).__init__(*args, **kwargs)
      self.fields['title'].label = 'Tapahtuman nimi'
      self.fields['start_date'].label = 'Aloituspäivä'
      self.fields['end_date'].label = 'Lopetuspäivä'
      self.fields['price'].label = 'Hinta'
      self.fields['bring_along'].label = 'Mitä mukaan?'
      self.fields['street_address'].label = 'Osoite'
      self.fields['city'].label = 'Kaupunki'
      self.fields['requirements'].label = 'Osallistujilta vaaditut esitiedot'
      self.fields['description'].label = 'Tapahtuman kuvaus'
      self.fields['organization'].label = 'Järjestäjä'
      self.fields['amount'].label = 'Osallistujien maksimimäärä'
      self.fields['signup_link'].label = 'Linkki omaan ilmoittautumiseen'

  start_date = forms.DateField(input_formats=['%d.%m.%Y'], widget=forms.DateInput(attrs={'class': 'startdate'}, format=('%d.%m.%Y')))
  end_date = forms.DateField(input_formats=['%d.%m.%Y'], required=False, widget=forms.DateInput(attrs={'class': 'enddate'}, format=('%d.%m.%Y')))
  start_hours = forms.IntegerField(required=True)
  start_minutes = forms.IntegerField(required=True)
  end_hours = forms.IntegerField(required=True)
  end_minutes = forms.IntegerField(required=True)

  class Meta:
    model = Event
    exclude = ['organizer', 'booked', 'time']
    widgets = {
      'start_date': forms.DateInput(format=('%d.%m.%Y')),
      'end_date': forms.DateInput(format=('%d.%m.%Y')),
      'bring_along': forms.TextInput(attrs={'placeholder': 'esim. kannettava tietokone, vanhempi'})
    }

class SignUpForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)
    self.fields['child'].label = 'Nimi'
    self.fields['guardian'].label = 'Huoltajan nimi'
    self.fields['age'].label = 'Ikä'
    self.fields['email'].label = 'Sähköposti'
    self.fields['phone'].label = 'Puhelinnumero'
    self.fields['other'].label = 'Muuta'

  class Meta:
    model = SignUp
    fields = ('child',
              'guardian',
              'age',
              'email',
              'phone',
              'other',)

class RegisterForm(forms.Form):
  email = forms.EmailField(label='Sähköposti')
  first_name = forms.CharField(label='Etunimi', max_length=100)
  last_name = forms.CharField(label='Sukunimi', max_length=100)
  password = forms.CharField(widget=forms.PasswordInput, label='Salasana')
  password_validate = forms.CharField(widget=forms.PasswordInput, label='Salasana uudestaan')

  def is_valid(self):
    valid = super(RegisterForm, self).is_valid()

    if not valid:
      return valid

    if self.cleaned_data['password'] != self.cleaned_data['password_validate']:
      self._errors['password'] = 'Salasanat eivät täsmää'
      return False

    return True

class LoginForm(forms.Form):
  email = forms.EmailField(label='Sähköposti')
  password = forms.CharField(widget=forms.PasswordInput, label='Salasana')

  def is_valid(self):
    valid = super(LoginForm, self).is_valid()

    if not valid:
      return valid

    user = authenticate(
      username=self.cleaned_data['email'],
      password=self.cleaned_data['password']
    )
    if not user or not user.is_active:
      self._errors['email'] = 'Sisäänkirjautuminen epäonnistui.'
      return False

    return True

  def login(self, request):
    email = self.cleaned_data['email']
    password = self.cleaned_data['password']
    user = authenticate(username=email, password=password)
    return user
