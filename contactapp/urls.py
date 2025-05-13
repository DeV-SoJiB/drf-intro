from django.urls import path, include
from .views import ContacViewSet, AuthorViewSet, BookViewSet

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

router = DefaultRouter()
router.register('contacts', ContacViewSet)
router.register("authors", AuthorViewSet)
router.register("books", BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='login'),
]

