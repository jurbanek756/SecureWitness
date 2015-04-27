from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.context_processors import csrf
from SecureWitness.models import CustomUser, Report
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Login.forms import SearchForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_active_check(user):
    return user.is_active

@login_required(redirect_field_name='Login', login_url='/Login/')
@user_passes_test(is_active_check, redirect_field_name='Login', login_url='/Login/')
def welcome(request):
    user = request.user
    latest_report_list = Report.objects.filter(private=False)
    for gr in user.groups.all():
      newList= Report.objects.filter(group__name= gr.name)
      latest_report_list = latest_report_list | newList
    if request.method == 'POST':
      if 'report' in request.POST:
         return HttpResponseRedirect('/report/')
      elif 'logout' in request.POST:
         logout(request)
         return HttpResponseRedirect('/Login/')
      elif 'Search' in request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
          keywords = request.POST['search'].split()
          ans = []
          ans.append([])
          i = 0
          j = 0
          for word in keywords:

            if word == "AND":
              i+=1
              ans.append([])
            elif word == "OR":
              pass
            else:
              ans[i].append(word)
          print(ans)
          for rep in latest_report_list:
            rep_keywords = str(rep)
            for k in range(len(ans)):
              if not any(word in rep_keywords for word in ans[k]):
                latest_report_list = latest_report_list.exclude(report_text_long= rep.report_text_long)
  
    else:
      form = SearchForm()
    #for each_report in latest_report_list:
    #   str(request.user.username) != each_report.
    context = {'latest_report_list': latest_report_list, 'form':form}
    return render(request, 'SecureWitness/Welcome.html', context)


@login_required(redirect_field_name='Login', login_url='/Login/')
@user_passes_test(is_active_check, redirect_field_name='Login', login_url='/Login/')
def profile(request):
    if request.method == 'POST':
        pass    
    else:
        user = request.user
        reports = Report.objects.filter(author = user.username)
    context = {'reports':reports, 'user':user}
    return render(request, 'SecureWitness/profile.html', context)
