from core.abstract.viewsets import AbstractViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from . serializers import UserSerializer
from . models import User


# Create your views here.
class UserViewSet(AbstractViewSet):
    http_method_names = ["path", "get"]
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        # Retrieve a list of users
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.exclude(is_superuser=True)

    def get_object(self):
        # Retrieve a single user
        obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj