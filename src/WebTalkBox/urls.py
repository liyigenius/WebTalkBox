from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebTalkBox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^talk/$', 'TalkMe.views.talk'),
    url(r'^show/$', 'TalkMe.views.show'),
    url(r'^delete/$', 'TalkMe.views.delete'),
)
