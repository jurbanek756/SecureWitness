import datetime
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import loader, RequestContext
from django.core.context_processors import csrf
from .forms import LoginForm, RegisterForm, ReportForm, GroupForm, MakeAdminsForm, BanUsersForm, AddToGroupForm, UserAddToGroupForm, DeleteReportForm, SearchForm
from SecureWitness.models import Report
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
import datetime
import SecureWitness
from SecureWitness.media import crypt



def is_active_check(user):
    return user.is_active

def is_reporter(user):
  gr = Group.objects.get(name='Reporter')
  return gr in user.groups

@login_required(redirect_field_name='Login', login_url='/Login/')
@user_passes_test(is_active_check, redirect_field_name='Login', login_url='/Login/')
def welcome(request):
    '''
    if request.method == 'POST':
        form = WelcomeForm(request.POST)
        if( 'adminButton' in request.POST):
            return HttpResponseRedirect('/AdminInterface/')
    '''
    user = request.user
    for gr in user__groups.all():
      latest_report_list = Report.objects.filter(group__name= gr.name)
    context1 = {'latest_report_list': latest_report_list,"user": user}
    return render(request, 'SecureWitness/Welcome.html', context1)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('//')

def yourReports(request):
    user = request.user
    reports = Report.objects.filter(author = user.username)
    return render(request, 'SecureWitness/reports.html',{"reports":reports} )

@login_required(redirect_field_name='Login', login_url='/Login/')
def edit_view(request, report_id):
    report = Report.objects.get(pk=report_id)
    if request.method== 'POST':
        form = ReportForm(request.POST, request.FILES, instance = report)
        if form.is_valid():
            if 'Submit' in request.POST:
                report.report_title = form['report_title'].value()
                report.incident_date = form['incident_date'].value()
                report.report_text_short = form['report_text_short'].value()
                report.file_upload = form['file_upload'].value()
                report.report_text_long = form['report_text_long'].value()
                report.location = form['location'].value()
                report.private = form['private'].value()
                report.keyword_list = form['keyword_list'].value()
                report.save()
                return HttpResponseRedirect('/Welcome/')

    else:
        form = ReportForm(instance = report )
    return render(request, 'SecureWitness/edit.html', {"report":report, "form": form})

@login_required(redirect_field_name='Login', login_url='/Login/')
def directory(request):
    user_list = User.objects.all()
    return render(request,'SecureWitness/directory.html', {"user_list":user_list} )

@login_required(redirect_field_name='Login', login_url='/Login/')
def admin_interface(request):
    return render(request,'SecureWitness/admin_interface.html' )

@login_required(redirect_field_name='Login', login_url='/Login/')
def addView(request):
    if request.method == 'POST':
        form=AddToGroupForm(request.POST)
        if form.is_valid():
            if 'Add to Group' in request.POST:
                user = User.objects.get(pk=request.POST['user'])
                group = Group.objects.get(pk=request.POST['group'])
                group.user_set.add(user)
                group.save()
                return HttpResponseRedirect('/AdminInterface/')
    else:
        form = AddToGroupForm()
    return render(request, 'SecureWitness/addGroup.html',{"form": form})


@login_required(redirect_field_name='Login', login_url='/Login/')
def userAddView(request):
    user = request.user
    groups = user.groups.all()
    if request.method == 'POST':
        form=UserAddToGroupForm(request.POST)
        if form.is_valid():
            if 'Add to Group' in request.POST:
                user = User.objects.get(pk=request.POST['user'])
                group = Group.objects.get(pk=request.POST['group'])
                group.user_set.add(user)
                group.save()
                return HttpResponseRedirect('/Welcome/')
    else:
        form = UserAddToGroupForm()
    return render(request, 'SecureWitness/userAddGroup.html',{"form": form, "groups":groups, "user": user})



@login_required(redirect_field_name='Login', login_url='/Login/')
def create_group(request):
    if request.method == 'POST':
        form=GroupForm(request.POST)
        if form.is_valid():
            if 'Create Group' in request.POST:
                name = request.POST['group']
                group = Group.objects.create(name=name)
                group.save()
                return HttpResponseRedirect('/AdminInterface/')
    else:
        form = GroupForm()
    return render(request, 'SecureWitness/create_group.html', {"form": form})

@login_required(redirect_field_name='Login', login_url='/Login/')
def ban_users(request):
    if request.method == 'POST':
        form=BanUsersForm(request.POST)
        if form.is_valid():
            if 'Ban' in request.POST:
                #username = request.POST['user']
                #user = User.objects.get(username=username)
                user = User.objects.get(pk=request.POST['user'])
                user.is_active=False
                user.save()
                return HttpResponseRedirect('/AdminInterface/')
    else:
        form =BanUsersForm()
    return render(request, 'SecureWitness/ban_users.html',{"form": form})

@login_required(redirect_field_name='Login', login_url='/Login/')
def make_admins(request):
    if request.method == 'POST':
        form=MakeAdminsForm(request.POST)
        if form.is_valid():
            if 'Make Admin' in request.POST:
                user = User.objects.get(pk=request.POST['user'])
                user.is_superuser = True
                user.is_staff = True
                user.save()
                return HttpResponseRedirect('/AdminInterface/')
    else:
        form = MakeAdminsForm()
    return render(request, 'SecureWitness/make_admins.html', {"form": form})


@login_required(redirect_field_name='Login', login_url='/Login/')
def delReportView(request):
    if request.method == 'POST':
        form=DeleteReportForm(request.POST)
        if form.is_valid():
            if 'Delete' in request.POST:
                report = Report.objects.get(pk=request.POST['report'])
                report.delete()
                #report.save()
                return HttpResponseRedirect('/AdminInterface/')
    else:
        form =DeleteReportForm()
    return render(request, 'SecureWitness/delete_reports.html',{"form": form})


@login_required(redirect_field_name='Login', login_url='/Login/')
def delYourReportView(request):
    user = request.user
    reports = Report.objects.filter(author = user.username)
    if 'Delete' in request.POST:
        report = Report.objects.get(pk=request.POST['report'])
        report.delete()
        return HttpResponseRedirect('/Welcome/')

    return render(request, 'SecureWitness/user_delete_reports.html', {"reports": reports, "user":user})


def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if 'Register' in request.POST:
            return HttpResponseRedirect('/Register/')
        elif form.is_valid():
            if 'Login' in request.POST:
                username = request.POST['user']
                password = request.POST['usrpass']
                user = authenticate(username = username, password = password)
                if user is not None and user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/Welcome/')
                else:
                    messages.error(request, 'Incorrect Authorization')
            else:
                print("Invalid login")
    else:
        form = LoginForm()
    return render(request,'Login/index.html', {'form':form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user= User.objects.create_user(form['username'].value(), form['usremail'].value(), form['usrpass'].value())
            '''
			user = User.objects.create_user(form['username'].value(), form['usremail'].value(), form['usrpass'].value())
			if form['reporter'].value():
				g = Group.objects.get(name='Reporter')
				g.user_set.add(user)
			else:
				g = Group.objects.get(name='Users')
				g.user_set.add(user)
			'''
            user.first_name = form['first'].value()
            user.last_name = form['last'].value()
            if form['reporter'].value():
              permission = Permission.objects.get(codename='add_report')
              user.user_permissions.add(permission)
            user.save()
            if form.is_valid():
                return HttpResponseRedirect('/Login/')
    else:
        form = RegisterForm()
    return render(request, 'Register/index.html', {'form':form})

@login_required(redirect_field_name='Login', login_url='/Login/')
def edit_view(request, report_id):
    report = Report.objects.get(pk=report_id)
    if request.method== 'POST':
        form = ReportForm(request.POST, request.FILES, instance = report)
        if form.is_valid():
            if 'Submit' in request.POST:
                report.report_title = form['report_title'].value()
                report.incident_date = form['incident_date'].value()
                report.report_text_short = form['report_text_short'].value()
                report.file_upload = form['file_upload'].value()
                report.report_text_long = form['report_text_long'].value()
                report.location = form['location'].value()
                report.private = form['private'].value()
                report.keyword_list = form['keyword_list'].value()
                report.save()
                return HttpResponseRedirect('/Welcome/')

    else:
        form = ReportForm(instance = report )
    return render(request, 'SecureWitness/edit.html', {"report":report, "form": form})

def yourReports(request):
    user = request.user
    reports = Report.objects.filter(author = user.username)
    return render(request, 'SecureWitness/reports.html',{"reports":reports} )

@login_required(redirect_field_name='Login', login_url='/Login/')
def delYourReportView(request):
    user = request.user
    reports = Report.objects.filter(author = user.username)
    if 'Delete' in request.POST:
        report = Report.objects.get(pk=request.POST['report'])
        report.delete()
        return HttpResponseRedirect('/Welcome/')

    return render(request, 'SecureWitness/user_delete_reports.html', {"reports": reports, "user":user})

@login_required(redirect_field_name='Login', login_url='/Login/')
@permission_required('SecureWitness.add_report')
def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid() and request.user.is_authenticated():

            user=request.user.username
            group= Group.objects.get(pk=form['group'].value())
            form = Report.objects.create_report(form['report_title'].value(), user, datetime.datetime.now(), form['incident_date'].value(), form['report_text_short'].value(), form['file_upload_1'].value(),form['file_upload_2'].value(), form['file_upload_3'].value(), form['file_upload_4'].value(), form['report_text_long'].value(), form['location'].value(), form['private'].value(), group, form['key'].value(), form['keyword_list'].value())
            form.save()
            #print(form.file_upload.name)
            #with open(form.file_upload, 'rb') as infile:
            #    infile.read(32)
            if form.private is True and form.key is not None:
                crypt.encrypt_file(crypt.getKey(form.key), form.file_upload)

            return HttpResponseRedirect('/Welcome/')
    else:
        form = ReportForm()
    return render(request, 'Report/report.html', {'form':form})
