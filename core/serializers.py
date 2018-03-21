from django.utils import timezone
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import (Role, Address, User, Contact, Department, Education, Doctor, Patient, Hospital, DaySchedule,
                     Appointment)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, style={'input_type': 'password'})

    class Meta:
        model = User
        # fields = ('url', 'username', 'email', 'first_name', 'last_name', 'password')
        fields = '__all__'
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


