from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'doctors', views.DoctorViewSet, basename='doctor')

urlpatterns = router.urls
