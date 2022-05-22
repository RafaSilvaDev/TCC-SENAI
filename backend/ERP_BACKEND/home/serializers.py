from dataclasses import field
from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customizes JWT default Serializer to add more information about user"""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        return token



class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Plant
        fields = "__all__"

class AreaSerializer(serializers.ModelSerializer):
    fk_plant = PlantSerializer(read_only=True)
    class Meta:
        many = True
        model = Area
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    fk_area = AreaSerializer(read_only=True)
    class Meta:
        many = True
        model = Team
        fields = "__all__"


class ProfileServiceSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = ProfileService
        fields = "__all__"

class AccessLevelSerializer(serializers.ModelSerializer):
    profiles = ProfileServiceSerializer(read_only=True, many=True)
    class Meta:
        many = True
        model = AccessLevel
        fields = "__all__"

class SimpleUserSerializer(serializers.ModelSerializer):
    fk_team = TeamSerializer(read_only = True, many=True)
    currentLevel = AccessLevelSerializer(read_only= True)
    user_img = serializers.SerializerMethodField('get_user_img_url')
    class Meta:
        many = True
        model = SimpleUser
        #fields = "__all__"
        exclude = ('password',)
    
    def get_user_img_url(self, obj):
        return obj.user_img.url


# class Colab_TeamSerializer(serializers.ModelSerializer):


#     fk_colab = SimpleUserSerializer(read_only=True)
#     fk_team = TeamSerializer(read_only=True)
#     class Meta:
#         many = True
#         model = Colab_Team
#         fields = "__all__"

class SystemSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = System
        fields = "__all__"

class SSMTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        many = True
        model = SSMType
        fields = "__all__"

class SSMSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField('get_file_url')
    miniImg = serializers.SerializerMethodField('get_img_url')
    fk_type = SSMTypeSerializer(read_only=True)
    class Meta:
        many = True
        model = SSM
        fields = "__all__"
    
    def get_file_url(self, obj):
        return obj.file.url

    def get_img_url(self, obj):
        return  obj.miniImg.url

class DDSSerializer(serializers.ModelSerializer):
    frontImg = serializers.SerializerMethodField('get_front_img_url')
    backImg = serializers.SerializerMethodField('get_back_img_url')

    #fk_type = DDSTypeSerializer(read_only=True)
    class Meta:
        many = True
        model = DDS
        fields = "__all__"

    def get_front_img_url(self, obj):
        try:
            return obj.frontImg.url
        except:
            return None


    def get_back_img_url(self, obj):
        try:
            return obj.backImg.url
        except:
            return None

# class SSMRandomOrderSerializer(serializers.ModelSerializer):
#     fk_ssm = SSMSerializer(read_only=True)
#     class Meta:
#         many = True
#         model = SSM
#         fields = "__all__"


class PatrolQuestSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = PatrolQuest
        fields = "__all__"







class PatrolAnswerSerializer(serializers.ModelSerializer):
    fk_patrolquest = PatrolQuestSerializer(read_only=True)
    class Meta:
        many = True
        model = PatrolAnswer
        fields = "__all__"







class PatrolDaySerializer(serializers.ModelSerializer):
    # fk_quests = PatrolQuestSerializer(read_only=True, many = True)
    fk_answers = PatrolAnswerSerializer(read_only=True, many = True)
    class Meta:
        many = True
        model = PatrolDay
        fields = "__all__"
        # exclude = ('fk_quests', )

class PatrolWeekSerializer(serializers.ModelSerializer):
    # fk_patrol = SimpleUserSerializer(read_only=True, many = False)
    # # fk_quests = PatrolQuestSerializer(read_only=True, many = True)
    # fk_answers = PatrolAnswerSerializer(read_only=True, many = True)
    fk_days = PatrolDaySerializer(read_only=True, many = True)
    class Meta:
        many = True
        model = PatrolWeek
        # fields = "__all__"
        exclude = ('fk_quests', )


class GeneratedAnswerFieldsSerializer(serializers.ModelSerializer):
    patrol_week_id = PatrolWeekSerializer(read_only=True, many = False)
    class Meta:
        many = True
        model = GeneratedAnswerFields
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        many = True
        model = Team
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    # location = LocationSerializer(read_only=True)
    class Meta:
        many = True
        model = Team
        fields = "__all__"

class TeamEventSerializer(serializers.ModelSerializer):
    fk_team = TeamSerializer(read_only=True)
    fk_event = EventSerializer(read_only=True) 
    class Meta:
        many = True
        model = TeamEvent
        fields = "__all__"
# class ProjectSerializer(serializers.ModelSerializer):
#     fk_owner = SimpleUserSerializer(read_only=True)
#     fk_team = TeamSerializer(read_only=True)
#     class Meta:
#         many = True
#         model = Project
#         fields = "__all__"

# class LocationScheduleSerializer(serializers.ModelSerializer):
#     class Meta:
#         many = True
#         model = LocationSchedule
#         fields = "__all__"

# class ScheduleEventSerializer(serializers.ModelSerializer):
#     fk_location = LocationScheduleSerializer(read_only=True)
#     fk_team = TeamSerializer(read_only=True)
#     fk_system = SystemSerializer(read_only=True)
#     class Meta:
#         many = True
#         model = ScheduleEvent
#         fields = "__all__"