from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.context_processors import csrf
from .forms import LoginForm
from .forms import RegisterForm
from django.contrib.auth.models import User, Group


def index(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			if 'Login' in request.POST:
				return HttpResponseRedirect('/test/')
			else:
				return HttpResponseRedirect('/Login/Register')
	else:
		form = LoginForm()
	return render(request,'Login/index.html', {'form':form})

def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		user = User.objects.create_user(form['username'].value(), form['usremail'].value(), form['usrpass'].value())
		if form['reporter'].value():
			g = Group.objects.get(name='Reporter')
			g.user_set.add(user)
		else:	
			g = Group.objects.get(name='Reporter')
			g.user_set.add(user)
		user.save()
		if form.is_valid():
			return HttpResponseRedirect('/test/')
	else:
		form = RegisterForm()
	return render(request, 'Register/index.html', {'form':form})
# Create your views here.
