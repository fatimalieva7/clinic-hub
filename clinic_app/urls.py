from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter
from clinic_app.views import Clinic, Category,Service, ReviewClinic

router = DefaultRouter()
router.register(r'clinics', Clinic, basename='clinic')
router.register(r'clinics-category', Category, basename='clinic-category')
router.register(r'services', Service, basename='service')
router.register(r'reviews', ReviewClinic, basename='review')

urlpatterns = router.urls