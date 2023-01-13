from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Note
from .models import KycInfo


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["titre", "description"]

class KycForm(forms.ModelForm):
    class Meta:
        model = KycInfo
        fields = ["nom", "nomFamille", "sex", "dateNaissance", "lieuNaissance","dateExpiration","mkz","description"]
