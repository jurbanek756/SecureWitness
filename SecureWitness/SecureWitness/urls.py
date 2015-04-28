from django.conf.urls import patterns, include, url
from django.contrib import admin

from Login import views

from SecureWitness import views
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SecureWitness.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'Welcome/$', views.welcome, name='welcome'),
    url(r'AdminInterface/$', 'Login.views.admin_interface', name='admin_interface'),
    url(r'Delete_Your_Report/$', 'Login.views.delYourReportView', name='delYourReportView'),
    url(r'YourReports/$', 'Login.views.yourReports', name='yourReports'),
    url(r'^(?P<report_id>[0-9]+)/edit/$', 'Login.views.edit_view', name='edit_view'),
    url(r'Add_User_To_Group/$', 'Login.views.userAddView', name='userAddView'),
    url(r'Add_to_Group/$', 'Login.views.addView', name='addView'),
    url(r'Create_Folder/$', 'Login.views.createFolder', name='createFolder'),
    url(r'Share_Folder/$', 'Login.views.shareFolder', name='shareFolder'),
    url(r'Delete_Folder/$', 'Login.views.deleteFolder', name='deleteFolder'),
    url(r'Add_to_Folder/$', 'Login.views.addToFolder', name='addToFolder'),
    url(r'Delete_Reports/$', 'Login.views.delReportView', name='delReportView'),
    url(r'Delete_Your_Report/$', 'Login.views.delYourReportView', name='delYourReportView'),
    url(r'YourReports/$', 'Login.views.yourReports', name='yourReports'),
    url(r'^(?P<report_id>[0-9]+)/edit/$', 'Login.views.edit_view', name='edit_view'),
    url(r'^(?P<report_id>[0-9]+)/report/$', 'Login.views.showReport', name='showReport'),
    url(r'^(?P<user_id>[0-9]+)/profile/$', 'Login.views.aProfile', name='aProfile'),
    url(r'Create_Groups/$', 'Login.views.create_group', name='create_group'),
    url(r'User_Directory/$', 'Login.views.directory', name='directory'),
    url(r'Ban_users/$', 'Login.views.ban_users', name='ban_users'),
    url(r'Make_admins/$', 'Login.views.make_admins', name='make_admins'),
    url(r'^$', include('Login.urls'), name='Login'),
    url(r'profile/$', views.profile, name='myprofile'),
    url(r'Logout/$', 'Login.views.logout_view', name='logout_view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Login/', include('Login.urls')),
    url(r'^Register/', 'Login.views.register', name='register'),
    url(r'^report/', 'Login.views.report', name='report'),
)


if settings.DEBUG:
    urlpatterns+= patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),

)
