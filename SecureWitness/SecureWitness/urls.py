from django.conf.urls import patterns, include, url
from django.contrib import admin
from SecureWitness import views
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SecureWitness.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'Welcome/$', views.welcome, name='welcome'),
    url(r'^$', include('Login.urls'), name='Login'),
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
