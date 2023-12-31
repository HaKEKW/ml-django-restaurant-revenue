from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile, PredictedModel
from django.forms import ModelForm

from django.forms.widgets import FileInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
         'profile_img': FileInput(),
         }


class ResultForm(ModelForm):
    class Meta:
        model = PredictedModel
        fields = '__all__'
        exclude = ['profile', 'results']
