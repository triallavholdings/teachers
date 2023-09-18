from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import (
    TeacherMember, Payment, License, WorkExperience, Education)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class TeacherMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeacherMember
        fields = '__all__'


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        
class LicenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = License
        fields = '__all__'


class WorkExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'
        

class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
