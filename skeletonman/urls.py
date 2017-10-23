from django.conf.urls import url

from . import views
from views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='index'),
    #url(r'^$', views.index, name='index'),
    url(r'^servo/$', views.servo_all),
    url(r'^servo/(?P<pk>[0-9]+)/$', views.servo_number),
]