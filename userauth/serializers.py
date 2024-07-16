from rest_framework import serializers
from skillxchange.models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model = CustomUser
        fields = "__all__"

    def create(self, validated_data):
        user = CustomUser(username = validated_data['username'],
                          name = validated_data['name'],
                          last_name = validated_data['last_name'],
                          is_basic = validated_data['is_basic'],
                          is_manager = validated_data['is_manager'],
                          is_admin=validated_data.get('is_admin', False),)
        
        user.set_password(validated_data['password'])
        user.save()
        return user