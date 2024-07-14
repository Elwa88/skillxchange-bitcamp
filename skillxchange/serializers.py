from rest_framework import serializers
from .models import Skills, CustomUser, Review, Enrollment


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = "__all__"
        read_only_fields = ['tutor']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def create_user(self,data):
        user = CustomUser(username = data['username'])
        user.set_password(data['password'])
        user.save()
        return user
    
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
        read_only_fields = ['student']