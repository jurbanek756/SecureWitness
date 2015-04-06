from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.context_processors import csrf
from .forms import LoginForm
from .forms import RegisterForm
<<<<<<< HEAD
from .models import ReportManager, Report
from .forms import ReportForm
=======
from SecureWitness.models import CustomUser, Report
>>>>>>> abc263547733fb1109379906ae6a1e18fd463e26
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages


def welcome(request):
    latest_report_list = Report.objects.order_by('-pub_date')[:5]
    context = {'latest_report_list': latest_report_list}
    return render(request, 'SecureWitness/Welcome.html', context)



def index(request):
<<<<<<< HEAD
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
					return HttpResponseRedirect('/Report/')
				else:
					messages.error(request, 'Incorrect Authorization')
			else:	
				print("Invalid login")
	else:
		form = LoginForm()
	return render(request,'Login/index.html', {'form':form})
=======
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
>>>>>>> abc263547733fb1109379906ae6a1e18fd463e26

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
            user.save()
            if form.is_valid():
                return HttpResponseRedirect('/Welcome/')
    else:
        form = RegisterForm()
    return render(request, 'Register/index.html', {'form':form})
# Create your views here.

def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form = Report.objects.create_report(form['report_title'].value(), form['author'].value(),
                                                form['pub_date'].value(), form['report_text_short'].value())
    else:
        form = ReportForm()
    return render(request, 'Report/report.html', {'form':form})
