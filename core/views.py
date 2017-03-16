from django.db.models import Avg, IntegerField
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet, ReadOnlyModelViewSet

from core.models import Book, Author
from core.serializers import BookSerializer, AuthorSerializer, LibrarySerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class LibraryModelViewSet(ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = LibrarySerializer


class StatisticViewSet(ViewSet):
    @staticmethod
    def retrieve(request):
        book_count = Book.objects.count()
        author_count = Author.objects.count()
        page_avg = Book.objects.aggregate(Avg('page_count', output_field=IntegerField()))

        response = {
            'books': book_count,
            'authors': author_count,
            **page_avg
        }

        return Response(response)
