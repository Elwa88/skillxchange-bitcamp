from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .permissions import CustomPermissions
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
    permission_classes = [CustomPermissions]
    def perform_create(self, serializer):
        serializer.save(tutor = self.request.user)

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]
    

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self,serializer):
        serializer.save(student = self.request.user)