from django.contrib import admin
from .models import *
from .forms import userForm

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('id', 'plant', 'plantAbrv')

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'area', 'areaAbrv')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'fk_area','fk_plant', 'qttMates' )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'date')

@admin.register(TeamEvent)
class TeamEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_team', 'fk_event')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'localName', 'businessPoint')


@admin.register(ProfileService)
class ProfileServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(AccessLevel)
class AccessLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    filter_horizontal = ('profiles',)

@admin.register(SimpleUser)
class SimpleUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'email')
    filter_horizontal = ('groups','fk_team','user_permissions')
    # list_display = ('id', )
    # form = userForm
    # class Media:
    #     js = ("js/selectColab.js",)

@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(SSMType)
class SSMTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type')


@admin.register(SSM)
class SSMAdmin(admin.ModelAdmin):
    list_display = ('id','title','fk_type')

@admin.register(PatrolQuest)
class PatrolQuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')

@admin.register(PatrolAnswer)
class PatrolAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'answerDay')

@admin.register(PatrolWeek)
class PatrolWeekAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_patrol')
    # filter_horizontal = ('fk_days',)
    filter_horizontal = ('fk_quests','fk_days')


@admin.register(PatrolDay)
class PatrolDayAdmin(admin.ModelAdmin):
    list_display = ('id',)
    filter_horizontal = ('fk_answers',)

@admin.register(DDS)
class DDSAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

# @admin.register(GeneratedAnswerFields)
# class GeneratedAnswerFieldsAdmin(admin.ModelAdmin):
#     list_display = ('id',)

