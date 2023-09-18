from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import (
    GroupSerializer, TeacherMemberSerializer, UserSerializer,
    PaymentSerializer, LicenseSerializer, WorkExperienceSerializer,
    EducationSerializer)

from .models import (
    TeacherMember, Payment, License, WorkExperience, Education)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeacherMemberViewSet(viewsets.ModelViewSet):

    queryset = TeacherMember.objects.all()
    serializer_class = TeacherMemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]


class LicenseViewSet(viewsets.ModelViewSet):

    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkExperienceViewSet(viewsets.ModelViewSet):

    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    permission_classes = [permissions.IsAuthenticated]


class EducationViewSet(viewsets.ModelViewSet):

    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated]
