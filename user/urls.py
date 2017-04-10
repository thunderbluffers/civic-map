from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'', include('django.contrib.auth.urls')),
    url(r'register/$', views.register, name='register'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    # url(r'login/$', auth_views.login),
    # url(r'logout/$', auth_views.logout),
    # url(r'password_change/$', auth_views.password_change),
    # url(r'password_change/done/$', auth_views.password_change_done),
    #url(r'password_reset/$', views.do_password_reset, name='password_reset'),
    #url(r'password_reset/done/$', views.password_reset_done, name='password_reset_done'),

    # url(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm),
    # url(r'reset/done/$', auth_views.password_reset_complete),
]
