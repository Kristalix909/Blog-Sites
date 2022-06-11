from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        models = User
        fields = ('username', 'email', 'password1','password2')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user