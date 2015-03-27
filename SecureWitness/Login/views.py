from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader

def index(request):
	return render_to_response('Login/index.html')

def register(request):
	return render_to_response('Register/index.html')
# Create your views here.
