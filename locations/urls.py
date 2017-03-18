from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'new$', views.new, name='new'),
    url(r'(?P<id>[0-9]+)/$', views.view, name='view'),
    url(r'(?P<id>[0-9]+)/edit$', views.edit, name='edit'),
    url(r'$', views.index, name='index'),
]
