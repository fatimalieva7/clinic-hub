from rest_framework.routers import DefaultRouter
from .views import (
    ClinicViewSet,
    CategoryViewSet,
    ServiceViewSet,
    ReviewClinicViewSet,
    AboutClinicViewSet,
    SheduleClinicViewSet,
    TeamMemberViewSet,
    ClinicAchievementViewSet
)

router = DefaultRouter()
router.register(r'clinics', ClinicViewSet, basename='clinic')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'reviews', ReviewClinicViewSet, basename='review')
router.register(r'about', AboutClinicViewSet, basename='about-clinic')
router.register(r'schedule', SheduleClinicViewSet, basename='schedule')
router.register(r'team', TeamMemberViewSet, basename='team-member')
router.register(r'achievements', ClinicAchievementViewSet, basename='clinic-achievement')

urlpatterns = router.urls