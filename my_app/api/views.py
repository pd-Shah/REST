from django.http import HttpResponse

from rest_framework import generics

from . import serializers
from my_app import models


def test(request, ):
    return HttpResponse('well done!')


class AuthorListApiView(generics.ListAPIView):
    serializer_class = serializers.AuthorSerializer

    def get_queryset(self, ):
        return models.Author.objects.all()
