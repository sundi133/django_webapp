from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trip.views.home', name='home'),
    # url(r'^trip/', include('trip.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#)

urlpatterns = patterns('',
(r'^trips/', include("trips.urls")),
(r'^search-form/$', 'trips.views.search_form'),
(r'^search/$', 'trips.views.search'),
)
