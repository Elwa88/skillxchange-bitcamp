from rest_framework import viewsets
from .permissions import SkillsPermissions, OtherPermissions
from .models import (
    Skills,
    CustomUser,
    Review,
    Enrollment,
)
from .serializers import (
    SkillSerializer,
    ReviewSerializer,
    EnrollmentSerializer,
    CustomUserSerializer,
)

class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [SkillsPermissions]
    def perform_create(self, serializer):
        serializer.save(tutor = self.request.user)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [OtherPermissions]
    

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [OtherPermissions]

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [OtherPermissions]
    
    def perform_create(self,serializer):
        serializer.save(student = self.request.user)