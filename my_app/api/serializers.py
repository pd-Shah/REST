from django.contrib.auth.models import User

from rest_framework import serializers
from my_app import models
from . import views

# class AuthorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     first_name = serializers.CharField(max_length=100)
#     last_name = serializers.CharField(max_length=100)
#     date_of_birth = serializers.DateField()
#     date_of_death = serializers.DateField('Died',)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return models.Author.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet`
#             instance, given the validated data.
#         """
#         instance.first_name = validated_data.get(
#                                 'first_name',
#                                 instance.first_name
#         )
#
#         instance.last_name = validated_data.get(
#                                 'last_name',
#                                 instance.last_name
#         )
#
#         instance.date_of_birth = validated_data.get(
#                                     'date_of_birth',
#                                     instance.date_of_birth
#         )
#
#         instance.date_of_death = validated_data.get(
#                                     'date_of_death',
#                                     instance.date_of_death
#         )
#
#         instance.save()
#         return instance

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     # authors = serializers.PrimaryKeyRelatedField(many=True, queryset=models.Author.objects.all())
#     authors_url =serializers.HyperlinkedIdentityField(view_name='my_app:api:author-detail-api-view')
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'authors_url', 'email', 'groups')


class AuthorSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # user_url = serializers.HyperlinkedIdentityField(view_name='my_app:api:user-detail-api-view')

    class Meta:
        model = models.Author
        fields = ['id', 'first_name', 'last_name',
                  'date_of_birth', 'date_of_death',
        ]
