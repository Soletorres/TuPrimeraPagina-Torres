from django import forms
from .models import Mensaje
from django.contrib.auth.models import User

class MensajeForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Para'
    )

    class Meta:
        model = Mensaje
        fields = ['destinatario', 'asunto', 'contenido']