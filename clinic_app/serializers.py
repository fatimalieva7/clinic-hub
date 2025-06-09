from rest_framework import  serializers
from .models import Clinic, Category, Service, ReviewClinic, AboutClinic, TeamMember, ClinicAchievement, SheduleClinic



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


class ClinicAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicAchievement
        fields = ['id', 'title', 'description', 'year', 'icon']


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'name', 'position', 'bio', 'photo', 'order']


class AboutClinicSerializer(serializers.ModelSerializer):
    team_members = TeamMemberSerializer(many=True, read_only=True)
    achievements = ClinicAchievementSerializer(many=True, read_only=True)
    logo_url = serializers.SerializerMethodField()

    class Meta:
        model = AboutClinic
        fields =  'id', 'title', 'description', 'mission', 'history', 
        'logo', 'logo_url', 'created_at', 'updated_at',
        'team_members', 'achievements'


class SheduleClinicSerializer(serializers.ModelSerializer):
    day_of_week_display = serializers.CharField(source='get_day_of_week_display', read_only=True)
    
    class Meta:
        model = SheduleClinic
        fields = ['__all__']
        extra_kwargs = {
            'clinic': {'read_only': True}  # Если клиника устанавливается автоматически
        }

    def validate(self, data):
        """
        Проверка что время закрытия больше времени открытия
        """
        if data['opening_time'] >= data['closing_time']:
            raise serializers.ValidationError("Время закрытия должно быть позже времени открытия")
        return data


