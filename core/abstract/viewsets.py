from rest_framework import viewsets
from rest_framework import filters


class AbstractViewSet(viewsets.ModelViewSet):
    """
    filter_backends allows you to define a list of classes that implement various filtering and ordering logic for
    the data returned by a view. These classes are applied in the order they appear in the list, and each class can
    perform specific filtering or ordering operations on the queryset before the data is returned to the client.
    """
    filter_backends =[filters.OrderingFilter]
    ordering_fields = ['updated', 'created']
    ordering = ['-updated']