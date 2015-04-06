from django import forms
from django.forms import ModelForm
from .models import Report, ReportManager

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

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['report_title', 'pub_date', 'report_text_short',
              'report_text_long', 'location', 'incident_date',
              'private']
