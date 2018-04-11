from django.conf.urls import url, include

from rest_framework_swagger.views import get_swagger_view

from . import views

swagger = get_swagger_view(title='Public API')

urlpatterns = [

    url(
        r'^author/$',
        view=views.AuthorList.as_view(),
        name='author-list-api-view'
    ),

    url(
        r'^author/(?P<pk>[0-9]+)/$',
        views.AuthorDetail.as_view(),
        name='author-detail-api-view'
    ),

    # url(r'^users/$', views.UserList.as_view(), name='user-list-api-view'),
    #
    # url(
    #     r'^users/(?P<pk>[0-9]+)/$',
    #     views.UserDetail.as_view(),
    #     name='user-detail-api-view'
    # ),

    url(r'^swagger/$', view=swagger, name='swagger'),
]
