from django.urls import include, path
from rest_framework import routers

from .views import (
    GroupViewSet, TeacherMemberViewSet, UserViewSet, PaymentViewSet,
    LicenseViewSet, WorkExperienceViewSet, EducationViewSet) 

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'teachermember', TeacherMemberViewSet)
router.register(r'payment', PaymentViewSet)
router.register(r'license', LicenseViewSet)
router.register(r'experience', WorkExperienceViewSet)
router.register(r'education', EducationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
