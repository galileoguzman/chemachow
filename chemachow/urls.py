from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chemachow.views.home', name='home'),
    # url(r'^chemachow/', include('chemachow.foo.urls')),
    url(r'^hola', 'chemachow.views.hola', name='hola'),
    url(r'^home', 'blog.views.probando', name='probando'),
    url(r'^inicio', 'blog.views.inicio', name='inicio'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
