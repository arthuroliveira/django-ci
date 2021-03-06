from django.conf.urls import patterns, include, url
from django.contrib import admin
import xadmin
from apps.homepage.views import *
xadmin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'arthur.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(xadmin.site.urls)),
    url(r'^foundation/', include('foundation.urls')),
    
    url(r'^$', HomepageView.as_view()),
)
