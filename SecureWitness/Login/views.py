from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm, ReportForm, GroupForm, MakeAdminsForm, BanUsersForm, AddToGroupForm
from SecureWitness.models import CustomUser, Report
from SecureWitness.media import crypt


@login_required(login_url='//')
def welcome(request):
    '''
    if request.method == 'POST':
        form = WelcomeForm(request.POST)
        if( 'adminButton' in request.POST):
            return HttpResponseRedirect('/AdminInterface/')
    '''
    username = request.user.name
    latest_report_list = Report.objects.order_by('-pub_date')[:5]
    context1 = {'latest_report_list': latest_report_list,"username": username}
    return render(request, 'SecureWitness/Welcome.html', context1)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('//')

def directory(request):
    user_list = CustomUser.objects.all()
    return render(request,'SecureWitness/directory.html', {"user_list":user_list} )

def admin_interface(request):
    return render(request,'SecureWitness/admin_interface.html' )

def addView(request):
    if request.method == 'POST':
        form=AddToGroupForm(request.POST)
        if form.is_valid():
            if 'Add to Group' in request.POST:
                username = request.POST['user']
                name = request.POST['group']
                user = CustomUser.objects.get(name=username)
                group = Group.objects.get(name=name)
                group.customuser_set.add(user)
                group.save()
                return HttpResponseRedirect('/AdminInterface/')
    else:
        form = AddToGroupForm()
    return render(request, 'SecureWitness/addGroup.html',{"form": form})

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

def ban_users(request):
    if request.method == 'POST':
        form=BanUsersForm(request.POST)
        if form.is_valid():
            if 'Ban' in request.POST:
                username = request.POST['user']
                user = CustomUser.objects.get(name=username)
                user.delete()
                return HttpResponseRedirect('/AdminInterface/')
    else:
        form =BanUsersForm()
    return render(request, 'SecureWitness/ban_users.html',{"form": form})

def make_admins(request):
    if request.method == 'POST':
        form=MakeAdminsForm(request.POST)
        if form.is_valid():
            if 'Make Admin' in request.POST:
                username = request.POST['user']
                user = CustomUser.objects.get(name=username)
                user.admin = True
                user.save()
                return HttpResponseRedirect('/AdminInterface/')
    else:
        form = MakeAdminsForm()
    return render(request, 'SecureWitness/make_admins.html', {"form": form})

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
                    print("Works")
                    return HttpResponseRedirect('/Welcome/')
                else:
                    print("The Fuck")
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
            user= CustomUser.objects.create_user(form['username'].value(), form['usremail'].value(), form['reporter'].value(), form['usrpass'].value())
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
            user.save()
            if form.is_valid():
                return HttpResponseRedirect('/Login/')
    else:
        form = RegisterForm()
    return render(request, 'Register/index.html', {'form':form})
# Create your views here.

@login_required(redirect_field_name='Login', login_url='/Login/')
def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid() and request.user.is_authenticated():
            user=request.user.first_name + " " + request.user.last_name
            form = Report.objects.create_report(form['report_title'].value(), user, form['pub_date'].value(), form['incident_date'].value(), form['report_text_short'].value(), form['file_upload'].value(), form['report_text_long'].value(), form['location'].value(), form['private'].value(), form['key'].value())
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
