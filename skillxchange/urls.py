from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, SkillsViewSet, CustomUserViewSet ,EnrollmentViewSet


router = DefaultRouter()
router.register(r'review',ReviewViewSet)
router.register(r'skills',SkillsViewSet)
router.register(r'users',CustomUserViewSet)
router.register(r'enrollment',EnrollmentViewSet)

urlpatterns = [
    path('',include(router.urls))
]
