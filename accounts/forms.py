from django import forms
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm

# class CustomLoginForm(LoginForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomLoginForm, self).__init__(*args, **kwargs)
#         self.fields['login'].widget = forms.TextInput(attrs=('class': 'form-input'))
