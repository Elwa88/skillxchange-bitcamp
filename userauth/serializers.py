from rest_framework import serializers
from skillxchange.models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model = CustomUser
        fields = ['name','last_name','username','password']

    def create_user(self,data):
        user = CustomUser(username = data['username'])
        user.set_password(data['password'])
        user.save()
        return user