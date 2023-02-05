from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email', 'password']


from .models import ques
class ques_add_serializer(serializers.ModelSerializer):
    class Meta:
        model=ques
        # fields='__all__'
        fields=['text','tags']