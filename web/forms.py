from django import forms
from web.models import Event, SignUp

class EventForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
      super(EventForm, self).__init__(*args, **kwargs)
      self.fields['title'].label = 'Tapahtuman nimi'
      self.fields['description'].label = 'Tapahtuman kuvaus'
      self.fields['start_date'].label = 'Tapahtuman alkamispäivä'
      self.fields['end_date'].label = 'Tapahtuman päättymispäivä'
      self.fields['street_address'].label = 'Tapahtumapaikan osoite'
      self.fields['city'].label = 'Kaupunki'
      self.fields['amount'].label = 'Osallistujien maksimimäärä'

  start_date = forms.DateField(input_formats=['%d.%m.%Y'], widget=forms.DateInput(attrs={'class': 'startdate'}, format=('%d.%m.%Y')))
  end_date = forms.DateField(input_formats=['%d.%m.%Y'], required=False, widget=forms.DateInput(attrs={'class': 'enddate'}, format=('%d.%m.%Y')))

  class Meta:
    model = Event
    fields = ('title',
              'description',
              'start_date',
              'end_date',
              'street_address',
              'city',
              'amount',)
    widgets = {
      'title': forms.TextInput(),
      'description': forms.TextInput(),
      'start_date': forms.DateInput(format=('%d.%m.%Y')),
      'end_date': forms.DateInput(format=('%d.%m.%Y')),
      'street_address': forms.TextInput(),
      'city': forms.TextInput(),
      'amount': forms.NumberInput(),
    }

class SignUpForm(forms.ModelForm):
  class Meta:
    model = SignUp
    fields = ('child',
              'guardian',
              'age',
              'email',
              'phone',
              'other',)
    widgets = {
      'child': forms.TextInput(attrs={'placeholder': 'Lapsen nimi'}),
      'guardian': forms.TextInput(attrs={'placeholder': 'Huoltajan nimi'}),
      'age': forms.NumberInput(attrs={'placeholder': 'Lapsen ikä'}),
      'email': forms.EmailInput(attrs={'placeholder': 'Sähköposti'}),
      'phone': forms.TextInput(attrs={'placeholder': 'Puhelinnumero'}),
      'other': forms.TextInput(attrs={'placeholder': 'Muuta'}),
    }

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
