from rest_framework import  serializers
from .models import Clinic, Category, Service, ReviewClinic


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'
      
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ReviewClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewClinic
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, data):
        user = self.context['request'].user
        if Review.objects.filter(user=user, clinic=data['clinic']).exists():
            raise serializers.ValidationError("Вы уже оставили отзыв")
        return data



