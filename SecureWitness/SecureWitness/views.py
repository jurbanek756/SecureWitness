from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.context_processors import csrf
from SecureWitness.models import CustomUser, Report
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib import messages


def welcome(request):
    latest_report_list = Report.objects.order_by('-pub_date')[:5]
    context = {'latest_report_list': latest_report_list}
    return render(request, 'SecureWitness/Welcome.html', context)



