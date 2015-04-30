from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.template import loader
from django.core.context_processors import csrf
from SecureWitness.models import CustomUser, Report
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Login.forms import SearchForm, AdvSearchForm
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
      elif 'AdvSearch' in request.POST:
         return HttpResponseRedirect('/search/') 
      elif 'Search' in request.POST:
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
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

def remoteLogin(request):
    if request.user.is_authenticated():
        return True
    else:
        return False


@login_required(redirect_field_name='Login', login_url='/Login/')
@user_passes_test(is_active_check, redirect_field_name='Login', login_url='/Login/')
def profile(request):
    if request.method == 'POST':
        pass    
    else:
        user = request.user
        search_form = SearchForm()
        reports = Report.objects.filter(author = user.username)
    context = {'reports':reports, 'user':user,'search_form':search_form}
    return render(request, 'SecureWitness/profile.html', context)
@login_required(redirect_field_name='Login', login_url='/Login/')
@user_passes_test(is_active_check, redirect_field_name='Login', login_url='/Login/')
def search(request):
    if request.method == 'POST':
        user = request.user
        latest_report_list = Report.objects.filter(private=False)
        for gr in user.groups.all():
            newList= Report.objects.filter(group__name= gr.name)
            latest_report_list = latest_report_list | newList
        form = AdvSearchForm(request.POST)
        if form.is_valid():
            title = form['title'].value()
            author = form['author'].value()
            loc = form['loc'].value()
            year = form['year'].value()
            for rep in latest_report_list:
                check1 = title not in rep.report_title and title!=''
                check2 = author not in rep.author and author!=''
                check3 = loc not in rep.location and loc!=''
                check4 = str(year) not in str(rep.incident_date) and str(year) != ''
                check5 = str(year) not in str(rep.pub_date) and str(year) !=''

                if check1 or check2 or check3 or check4 or check5:
                    latest_report_list = latest_report_list.exclude(report_text_long= rep.report_text_long)
        form = AdvSearchForm()
        context= {'form':form, 'latest_report_list':latest_report_list}
        return render(request, 'SecureWitness/search.html', context)
    else:
        form = AdvSearchForm()
    return render(request, 'SecureWitness/search.html', {'form':form})
