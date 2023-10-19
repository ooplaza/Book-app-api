from rest_framework.routers import SimpleRouter
from core.book.viewsets import BookViewSet

# Instantiate
router = SimpleRouter()
router.register(r"books", BookViewSet, basename='book-list')

# Viewsets
urlpatterns = [
    *router.urls
]