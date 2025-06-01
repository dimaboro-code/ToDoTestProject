from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TechParkParseView, TechParkCompanyViewSet

router = DefaultRouter()
router.register('companies', TechParkCompanyViewSet, basename='techpark-company')

urlpatterns = [
    path('parse/', TechParkParseView.as_view(), name='techpark-parse'),
    path('', include(router.urls)),
]
