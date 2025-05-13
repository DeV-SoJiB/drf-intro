from django.shortcuts import render
from .models import Contacts, Authors, Books

from .serializers import ContactSerializer, AuthorSerializer, BookSerializer
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
class ContacViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer


# from django_filters import FilterSet, NumberFilter


# class BookFilter(FilterSet):
#     min_price = NumberFilter(field_name="price", lookup_expr="gte")
#     max_price = NumberFilter(field_name="price", lookup_expr="lte")

#     class Meta:
#         models = Book
#         fields = ["min_price", "max_price"]

from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size = 5

class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter, 
        OrderingFilter
    ]
    filterset_fields = ['author', 'title']
    search_fields = ['title']
    ordering_fields = ['title', 'author']
    pagination_class = MyPagination


