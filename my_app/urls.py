from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/',
        include('my_app.api.urls', namespace='my_app'), name='myapp_api'),
]
