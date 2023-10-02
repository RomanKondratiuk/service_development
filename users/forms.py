from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

        def save(self, commit=True):
            user = super().save(commit=False)
            user.generate_email_verification_token()
            if commit:
                user.save()
            return user


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar')

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['password'].widget = forms.HiddenInput()
