from rest_framework import serializers
from .models import Doctor
from users_app.serializers import UserRegisterSerializer

def get_experience_display(obj):
    return f"{obj.experience} лет"


class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # покажет email
    experience_display = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = '__all__'

