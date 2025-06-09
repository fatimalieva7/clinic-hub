from rest_framework import viewsets, permissions
from .models import Clinic, Category, Service, ReviewClinic, AboutClinic, TeamMember, ClinicAchievement, SheduleClinic
from .serializers import (
    ClinicSerializer, 
    CategorySerializer, 
    ServiceSerializer, 
    ReviewClinicSerializer,
    AboutClinicSerializer, 
    TeamMemberSerializer,
    ClinicAchievementSerializer, 
    SheduleClinicSerializer
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all() 
    serializer_class = ServiceSerializer

class ReviewClinicViewSet(viewsets.ModelViewSet):
    queryset = ReviewClinic.objects.all()
    serializer_class = ReviewClinicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AboutClinicViewSet(viewsets.ModelViewSet):
    queryset = AboutClinic.objects.all()
    serializer_class = AboutClinicSerializer
    http_method_names = ['get']

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.filter(is_visible=True).order_by('order')
    serializer_class = TeamMemberSerializer
    http_method_names = ['get']

class ClinicAchievementViewSet(viewsets.ModelViewSet):
    queryset = ClinicAchievement.objects.all()
    serializer_class = ClinicAchievementSerializer
    http_method_names = ['get']

class SheduleClinicViewSet(viewsets.ModelViewSet):
    queryset = SheduleClinic.objects.all()
    serializer_class = SheduleClinicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
