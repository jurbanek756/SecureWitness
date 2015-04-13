from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.context_processors import csrf
from .forms import LoginForm
from .forms import RegisterForm
from .models import ReportManager, Report
from .forms import ReportForm
from SecureWitness.models import CustomUser, Report
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, get_user
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def welcome(request):
    latest_report_list = Report.objects.order_by('-pub_date')[:5]
    context = {'latest_report_list': latest_report_list}
    return render(request, 'SecureWitness/Welcome.html', context)



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
                return HttpResponseRedirect('/Welcome/')
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
            form = Report.objects.create_report(form['report_title'].value(), user, form['pub_date'].value(), form['incident_date'].value(), form['report_text_short'].value(), form['file_upload'].value(), form['report_text_long'].value(), form['location'].value(), form['private'].value())
            form.save()
            return HttpResponseRedirect('/Welcome/')
    else:
        form = ReportForm()
    return render(request, 'Report/report.html', {'form':form})
