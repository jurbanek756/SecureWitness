from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from SecureWitness.models import Report, ReportManager
from django.forms import ModelForm, Textarea
from django.contrib.admin.widgets import AdminDateWidget



class ShareFolderForm(forms.Form):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), label='Group Name', required = 'True')

class CreateFolderForm(forms.Form):
    name = forms.CharField(label="Folder Name", required='True')

class GroupForm(forms.Form):
    group = forms.CharField(label='Group Name', required='True')


class SearchForm(forms.Form):
    search = forms.CharField(label='Search', required=True)

class AdvSearchForm(forms.Form):
    title = forms.CharField(label='Title', required=False)
    author = forms.CharField(label='Author', required=False)
    loc = forms.CharField(label='Location', required=False)
    year = forms.IntegerField(label='Year', required=False, min_value=1990, max_value=2015)

class DeleteReportForm(forms.Form):
    report = forms.ModelChoiceField(queryset=Report.objects.all(), label='Report', required=True)


class UserAddToGroupForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label='Username', required=True)
    #group = forms.ModelChoiceField(queryset=Group.objects.filter(), label='Group Name', required = 'True')

class AddToGroupForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label='Username', required=True)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), label='Group Name', required = 'True')


class BanUsersForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label='Username', required=True)


class MakeAdminsForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label='Username', required=True)


class LoginForm(forms.Form):
    user = forms.CharField(label='', required=True,
                           widget=forms.TextInput(attrs={'placeholder':'User Name'}))
    usrpass = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}), required=True)

class RegisterForm(forms.Form):
    first = forms.CharField(label='First')
    last = forms.CharField(label='Last')
    reporter = forms.BooleanField(label='Reporter', required=False)
    username = forms.CharField(label='Username')
    usrpass = forms.CharField(label='Password', widget=forms.PasswordInput)
    usremail = forms.EmailField(label='Email')


class ReportForm(ModelForm):
    #pub_date = forms.DateField(widget=AdminDateWidget)

    class Meta:
        model = Report

        fields = ['report_title', 'report_text_short',
                  'report_text_long', 'location', 'incident_date',
                  'private', 'file_upload_1', 'file_upload_2', 'file_upload_3', 'file_upload_4', 'group', 'key', 'keyword_list']


        widgets = {
            'report_text_long': Textarea(attrs={'cols': 50, 'rows': 8})
        }
