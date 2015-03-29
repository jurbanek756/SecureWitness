from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SecureWitness.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('Login.urls'), name='Login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Login/', include('Login.urls')),
    url(r'^Register/', include('Login.urls'))


)
