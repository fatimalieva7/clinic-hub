from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'appointments', views.AppointmentViewSet, basename='appointment')
router.register(r'users', views.User, basename='user')
router.register(r'user-verify', views.SMSVerification, basename='user_verify')



urlpatterns = router.urls