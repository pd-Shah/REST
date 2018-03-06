from django.conf.urls import url

from . import views

from rest_framework_swagger.views import get_swagger_view

swagger = get_swagger_view(title='Public API')

urlpatterns = [
    url(r'^test/$', view=views.test, name='test'),
    url(
        r'^author/$',
        view=views.AuthorListApiView.as_view(),
        name='author-list-api-view'
    ),
    url(r'^swagger/$', view=swagger, name='swagger'),
]
