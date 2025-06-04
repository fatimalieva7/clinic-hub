from rest_framework import viewsets
from .serializers import ClinicSerializer, CategorySerializer
from  .models import Clinic, Category, Service
from .serializers import ServiceSerializer
from .serializers import ReviewClinicSerializer
from .models import ReviewClinic
from rest_framework import permissions



class Category(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class Clinic(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class Service(viewsets.ModelViewSet):
    queryset = Service.objects.all() 
    serializer_class = ServiceSerializer

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }
        return super().get_serializer(*args, **kwargs)

class ReviewClinic(viewsets.ModelViewSet):
    queryset = ReviewClinic.objects.all()
    serializer_class = ReviewClinicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)