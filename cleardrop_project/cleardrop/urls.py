from django.urls import path, include

from rest_framework.routers import DefaultRouter

from cleardrop.views import labs_views, tests_views

router = DefaultRouter()

router.register(r'labs', labs_views.LabsViewSet, basename='labs')
router.register(r'tests', tests_views.TestsViewSet, basename='tests')

urlpatterns = [
    path('', include(router.urls))
]
