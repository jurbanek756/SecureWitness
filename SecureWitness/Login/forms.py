from django import forms

class LoginForm(forms.Form):
	user = forms.CharField(label='Username', required=False)
	usrpass = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)

class RegisterForm(forms.Form):
	reporter = forms.BooleanField(label='Reporter', required=False)
	username=forms.CharField(label='Username')
	usrpass = forms.CharField(label='Password', widget = forms.PasswordInput)
	usremail = forms.EmailField(label='Email')
