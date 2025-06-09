from rest_framework import serializers
from .models import  SMSVerification, User



class SMSVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSVerification
        fields = ['email', 'code']


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username',  'email', 'role', 'is_active', 'username']


# class AppointmentCreateSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(write_only=True)
#     verification_code = serializers.CharField(write_only=True, max_length=4)
    
#     class Meta:
#         model = Appointment
#         fields = '__all__'
#         read_only_fields = ['status']
    
#     def validate(self, data):
#         # Проверка кода подтверждения
#         verification_data = {
#             'email': data['email'],
#             'code': data['verification_code']
#         }
#         sms_serializer = SMSVerificationSerializer(data=verification_data)
#         sms_serializer.is_valid(raise_exception=True)
        
#         # Проверка что пользователь существует
#         User = apps.get_model('accounts_app.User')
#         try:
#             user = User.objects.get(email=data['email'])
#         except User.DoesNotExist:
#             raise ValidationError("Пользователь с таким email не зарегистрирован")
        
#         # Проверка что врач доступен в это время
#         doctor = data['doctor']
#         date = data['date']
#         time = data['time']
        
#         if Appointment.objects.filter(
#             doctor=doctor,
#             date=date,
#             time=time,
#             status__in=['pending', 'confirmed']
#         ).exists():
#             raise ValidationError("Это время уже занято")
            
#         return data
    
#     def create(self, validated_data):
#         User = apps.get_model('accounts_app.User')
#         user = User.objects.get(email=validated_data.pop('email'))
#         validated_data.pop('verification_code')
        
#         appointment = Appointment.objects.create(
#             user=user,
#             **validated_data
#         )
#         return appointment

# class AppointmentSerializer(serializers.ModelSerializer):
#     doctor_name = serializers.CharField(source='doctor.get_full_name', read_only=True)
    
#     class Meta:
#         model = Appointment
#         fields = '__all__'
#         read_only_fields = ['created_at', 'updated_at']



