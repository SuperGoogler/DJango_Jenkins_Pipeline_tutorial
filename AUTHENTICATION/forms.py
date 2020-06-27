from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    Photo = forms.ImageField( max_length=100)  #widget=forms.ClearableFileInput(attrs={'multiple': True}),
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    country = forms.CharField(max_length=100)
    State = forms.CharField(max_length=100)
    District = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=10)

    class Meta:
        model = UserProfile
        fields = ('Photo', 'dob', 'country', 'State', 'District', 'phone')


