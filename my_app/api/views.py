from django.http import HttpResponse, Http404

from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from my_app import models

# def test(request, ):
#     return HttpResponse('well done!')
#
#
# class AuthorListApiView(generics.ListAPIView):
#     serializer_class = serializers.AuthorSerializer
#
#     def get_queryset(self, ):
#         return models.Author.objects.all()


# @api_view(['GET', 'POST'])
# def author_list(request):
#     """
#     List all code Authors, or create a new author.
#     """
#     if request.method == 'GET':
#         authors = models.Author.objects.all()
#         serializer = serializers.AuthorSerializer(authors, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = serializers.AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     """
#     Retrieve, update or delete a code author.
#     """
#     try:
#         author = models.Author.objects.get(pk=pk)
#     except models.Author.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = serializers.AuthorSerializer(author)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = serializers.AuthorSerializer(author, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class AuthorList(generics.GenericAPIView):
    """
    List all authors, or create a new Author.
    """

    serializer_class = serializers.AuthorSerializer
    
    def get(self, request, format=None):
        authors = models.Author.objects.all()
        serializer = serializers.AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(generics.GenericAPIView):
    """
    Retrieve, update or delete a author instance.
    """

    serializer_class = serializers.AuthorSerializer

    def get_object(self, pk):
        try:
            return models.Author.objects.get(pk=pk)
        except models.Author.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = serializers.AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = serializers.AuthorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        author = self.get_object(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
