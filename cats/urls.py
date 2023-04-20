from django.contrib import admin
from django.urls import path, include

from .views import CatViewSet, OwnerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)

urlpatterns = [
    # path('cats/', CatListAPI.as_view()),
    # path('cats/<int:pk>/', cat_detail),
    path('', include(router.urls)),
]