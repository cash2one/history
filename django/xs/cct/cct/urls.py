from django.conf.urls import patterns, url
from settings import STATIC_ROOT

urlpatterns = patterns('cct.views',
    url(r'^$', 'index', name='index'),
    url(r'^about/$', 'about', name='about'),
    url(r'^admin/$', 'admin', name='admin'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^islogin/$', 'islogin', name='islogin'),
    url(r'^about/apt/$', 'aboutapt', name='aboutapt'),
    url(r'^service/$', 'service', name='service'),
    url(r'^service/group-(?P<num>\d+)/$', 'servicegroup', name='servicegroup'),
    url(r'^service/usa/$', 'serviceusa', name='serviceusa'),
    url(r'^service/tha/$', 'servicetha', name='servicetha'),
    url(r'^service/pcs/$', 'servicepcs', name='servicepcs'),
    url(r'^hospital/$', 'hospital', name='hospital'),
    url(r'^hospital/(?P<cid>\d+)/$', 'hospital', name='hospital'),
    url(r'^doctor/$', 'doctor', name='doctor'),
    url(r'^doctor/(?P<htp>\d+)/$', 'doctor', name='doctor'),
    url(r'^doctor/(?P<page>\d+).htm$', 'doctor', name='doctor'),
    url(r'^doctor/(?P<hid>\d+)-(?P<page>\d+).htm$', 'doctor', name='doctor'),
    url(r'^knowledge/$', 'knowledge', name='knowledge'),
    url(r'^knowledge/(?P<page>\d+).htm$', 'knowledge', name='knowledge'),
    url(r'^news/$', 'news', name='news'),
    url(r'^news/(?P<page>\d+).htm$', 'news', name='news'),
    url(r'^contact/$', 'contact', name='contact'),
    url(r'^cost/$', 'cost', name='cost'),
    url(r'^detail/(?P<kwd>\w+)-(?P<did>\d+).html$', 'detail', name='detail'),
)
urlpatterns += patterns('cct.admin',
    url(r'^upload/$', 'upload', name='upload'),
    url(r'^fileload/$', 'fileload', name='fileload'),
    url(r'^fileload2/$', 'fileload2', name='fileload2'),
    url(r'^gethospital/$', 'gethospital', name='gethospital'),
    url(r'^gethptdetail/$', 'gethptdetail', name='gethptdetail'),
    url(r'^uphospital/$', 'uphospital', name='uphospital'),
    url(r'^getdoctor/$', 'getdoctor', name='getdoctor'),
    url(r'^getdctdetail/$', 'getdctdetail', name='getdctdetail'),
    url(r'^updoctor/$', 'updoctor', name='updoctor'),
    url(r'^getnews/$', 'getnews', name='getnews'),
    url(r'^upnews/$', 'upnews', name='upnews'), 
    url(r'^getnewsdetail/$', 'getnewsdetail', name='getnewsdetail'),  
    url(r'^saveImg/$', 'saveImg', name='saveImg'),  
)
urlpatterns += patterns('cct.img',
    url(r'^img/(.*?)$', 'img', name='img'),                        
)
urlpatterns += patterns('',url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': STATIC_ROOT,}),)