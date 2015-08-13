from django.forms import ModelForm, TextInput, DateInput, EmailInput, NumberInput, DateField
from web.models import Event, SignUp

class EventForm(ModelForm):
  start_date = DateField(input_formats=['%d.%m.%Y'], widget=DateInput(attrs={'class': 'startdate'}, format=('%d.%m.%Y')))
  end_date = DateField(input_formats=['%d.%m.%Y'], required=False, widget=DateInput(attrs={'class': 'enddate'}, format=('%d.%m.%Y')))

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
      'title': TextInput(attrs={'placeholder': 'Otsikko'}),
      'description': TextInput(attrs={'placeholder': 'Kuvaus'}),
      'start_date': DateInput(format=('%d.%m.%Y')),
      'end_date': DateInput(format=('%d.%m.%Y')),
      'street_address': TextInput(attrs={'placeholder': 'Osoite'}),
      'city': TextInput(attrs={'placeholder': 'Kaupunki'}),
      'amount': NumberInput(attrs={'placeholder': 'Osallistujien lukumäärä'}),
    }

class SignUpForm(ModelForm):
  class Meta:
    model = SignUp
    fields = ('child',
              'guardian',
              'age',
              'email',
              'phone',
              'other',)
    widgets = {
      'child': TextInput(attrs={'placeholder': 'Lapsen nimi'}),
      'guardian': TextInput(attrs={'placeholder': 'Huoltajan nimi'}),
      'age': NumberInput(attrs={'placeholder': 'Lapsen ikä'}),
      'email': EmailInput(attrs={'placeholder': 'Sähköposti'}),
      'phone': TextInput(attrs={'placeholder': 'Puhelinnumero'}),
      'other': TextInput(attrs={'placeholder': 'Muuta'}),
    }
