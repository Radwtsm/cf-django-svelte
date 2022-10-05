
from django import forms
from api.models import DatiPersona


class DatiPersonaForm(forms.ModelForm):

    class Meta:
        model = DatiPersona
        fields = ['surname', 'name', 'sex',
                  'birthdate', 'birthplace']

        error_messages = {

        }
