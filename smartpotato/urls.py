from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'matchmaker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # ANOTHER METHOD TO SERVE STATIC FILES #
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
    #    'document_root': settings.STATIC_ROOT}),
    #(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    #    'document_root': settings.MEDIA_ROOT}),

    url(r'^admin/', include(admin.site.urls)),
    #used to overwrite registration.auth_urls because in django 1.6 django.contrib.auth.views use different urls
    url(r'^accounts/password/change/$', auth_views.password_change, name='password_change'),
    url(r'^accounts/password/change/done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^accounts/password/reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^accounts/password/reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^accounts/password/reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),

    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', 'profiles.views.home', name='home'),
    url(r'^members/(?P<username>\w+)/$', 'profiles.views.user_profile', name='user_profile'),
    url(r'^upload_image/(?P<username>\w+)/$', 'profiles.views.image_upload', name='upload_image'),
    url(r'^receipt_tips/$', 'profiles.views.receipt_tips', name='receipt_tips'),
    url(r'^dashboard/(?P<username>\w+)/$', 'profiles.views.dashboard', name='dashboard'),
    url(r'^dashboard/sugar/(?P<username>\w+)/$', 'profiles.views.sugar_dashboard', name='sugar_dashboard'),
    url(r'^dashboard/trend/(?P<username>\w+)/$', 'profiles.views.trend_dashboard', name='trend_dashboard'),
    url(r'^dashboard/recm/(?P<username>\w+)/$', 'profiles.views.recm_dashboard', name='recm_dashboard'),
    url(r'^dashboard/detailed_data/(?P<username>\w+)/$', 'profiles.views.detailed_data', name='detailed_data'),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
