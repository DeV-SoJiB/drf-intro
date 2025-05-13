from rest_framework import serializers

from .models import Contacts, Authors, Books

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'name', 'email', 'phone_number', 'address']

        extra_kwargs = {
            "name" : {
                "min_length": 5,

                "error_messages": {
                    "min_length": "Please enter more than 5 characters"
                }
            }
        }


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'author']