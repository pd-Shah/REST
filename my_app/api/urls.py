from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^test/$', view=views.test, name='test'),
]
