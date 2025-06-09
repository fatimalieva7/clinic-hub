from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'appointments', views.AppointmentViewSet, basename='appointment')
router.register(r'users', views.UserApiView, basename='user')
router.register(r'user-verify', views.SMSVerificationApiView, basename='user_verify')



urlpatterns = router.urls