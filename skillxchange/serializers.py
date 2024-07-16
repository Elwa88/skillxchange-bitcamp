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
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"
        read_only_fields = ['student']

    def validate(self, data):
        skill = data['skill']

        if skill.current_students >= skill.limit:
            raise serializers.ValidationError("error in limit")
        
        return data
    
    def create(self, validated_data):
        skill = validated_data['skill']
        skill.current_students += 1
        skill.save()
        return super().create(validated_data)