from django import forms

class adminForm:
    group = forms.CharField(label='Group Name', required = 'True')


class LoginForm(forms.Form):
	user = forms.CharField(label='Username', required=True)
	usrpass = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

class RegisterForm(forms.Form):
	reporter = forms.BooleanField(label='Reporter', required=False)
	username=forms.CharField(label='Username')
	usrpass = forms.CharField(label='Password', widget = forms.PasswordInput)
	usremail = forms.EmailField(label='Email')
