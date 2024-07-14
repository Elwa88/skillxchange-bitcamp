from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .serializers import UserRegistrationSerializer
from skillxchange.models import CustomUser
from rest_framework.permissions import AllowAny
# Create your views here.

class UserRegistrationView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes =[AllowAny]
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "user": {
                    "username": user.username,
                    }
                }, status= HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)