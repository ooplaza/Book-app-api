from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from . serializers import BookSerializer
from . models import Book


# Create your views here.
class BookViewSet(ModelViewSet):
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        :return: Books
        """
        queryset = Book.objects.filter(release_year__lt=20)
        return queryset

    def get_object(self):
        """ Fetch a single project. """
        obj = Book.objects.get_object_by_public_id(self.kwargs["pk"])
        # It is responsible for checking the object-level permissions for a given request and object.
        self.check_object_permissions(self.request, obj)
        return obj

