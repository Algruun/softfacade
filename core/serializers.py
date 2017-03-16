from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from core.models import Book, Author


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['author', 'title', 'page_count']


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class LibrarySerializer(ModelSerializer):
    author = StringRelatedField(source='author.name')

    class Meta:
        model = Book
        fields = ['author', 'title', 'page_count']
