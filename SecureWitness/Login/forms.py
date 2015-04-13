from django import forms
from django.forms import ModelForm
from SecureWitness.models import Report, ReportManager
from django.forms import ModelForm, Textarea



class GroupForm(forms.Form):
    group = forms.CharField(label='Group Name', required = 'True')
'''
class WelcomeForm(forms.Form):
    admin_button = forms.()
'''

class AddToGroupForm(forms.Form):
    user = forms.CharField(label='Username', required=True)
    group = forms.CharField(label='Group Name', required = 'True')

class BanUsersForm(forms.Form):
    user = forms.CharField(label='Username', required=True)

class MakeAdminsForm(forms.Form):
    user = forms.CharField(label='Username', required=True)

class LoginForm(forms.Form):
	user = forms.CharField(label='Username', required=True)
	usrpass = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

class RegisterForm(forms.Form):
	first = forms.CharField(label='First')
	last = forms.CharField(label='Last')
	reporter = forms.BooleanField(label='Reporter', required=False)
	username=forms.CharField(label='Username')
	usrpass = forms.CharField(label='Password', widget = forms.PasswordInput)
	usremail = forms.EmailField(label='Email')

class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['report_title', 'pub_date', 'report_text_short',
              'report_text_long', 'location', 'incident_date',
              'private', 'file_upload']
        widgets = {
            'report_text_long':Textarea(attrs={'cols': 80, 'rows': 20}),
        }
