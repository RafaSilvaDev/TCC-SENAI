from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from .views import *


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    path('pdf/', fetchpdf.as_view()),
    # path('media/', include('media')),
    path('search/', search_view.as_view(), name='search'),
    path('filter/ssm/', search_view_ssm.as_view(), name='search'),
    

    #  ALL PLANTS IN DB
    path('plants/', PlantApiView.as_view(), name="plants"),
    #  FILTERED PLANT BY PRIMARY KEY
    path('plants/<int:id>', PlantApiView.as_view(), name="plantsFilter"),

    #  ALL AREAS IN DB
    path('areas/', AreaApiView.as_view(), name="areas"),
    #  FILTERED AREA BY PRIMARY KEY
    path('areas/<int:id>', AreaApiView.as_view(), name="areasFilter"),

    #  ALL TEAMS IN DB
    path('teams/', TeamApiView.as_view(), name="teams"),
    #  FILTERED TEAM BY PRIMARY KEY
    path('teams/<int:id>', TeamApiView.as_view(), name="teamsFilter"),

    #  ALL PROFILE SERVICES IN DB
    path('profileservices/', ProfileServiceApiView.as_view(), name="profileservices"),
    #  FILTERED PROFILE SERVICE BY PRIMARY KEY
    path('profileservices/<int:id>', ProfileServiceApiView.as_view(), name="profileservicesFilter"),

    #  ALL ACCESS LEVELS IN DB
    path('accesslevels/', AccessLevelApiView.as_view(), name="accesslevels"),
    #  FILTERED ACCESS LEVEL BY PRIMARY KEY
    path('accesslevels/<int:id>', AccessLevelApiView.as_view(), name="accesslevelsFilter"),

    #  ALL SIMPLE USERS IN DB
    path('simpleusers/', SimpleUserApiView.as_view(), name="simpleusers"),
    #  FILTERED SIMPLE USER BY PRIMARY KEY
    path('simpleusers/<int:id>', SimpleUserApiView.as_view(), name="simpleusersFilter"),

    #  ALL SYSTEMS IN DB
    path('systems/', SystemApiView.as_view(), name="systems"),
    #  FILTERED SYSTEM BY PRIMARY KEY
    path('systems/<int:id>', SystemApiView.as_view(), name="systemsFilter"),

    #  ALL SSM TYPES IN DB
    path('ssmtypes/', SSMTypeApiView.as_view(), name="ssmTypes"),
    #  FILTERED SSM TYPE BY PRIMARY KEY
    path('ssmtypes/<int:id>', SSMTypeApiView.as_view(), name="ssmTypesFilter"),

    # GET ALL SSMs IN DB
    path('ssm/', SSMApiView.as_view(), name="ssm"),
    # GET FILTERED DDS BY PRIMARY KEY
    path('ssm/<int:id>', SSMApiView.as_view(), name="ssmFilter"),

    #  ALL DDSs IN DB
    path('dds/', DDSApiView.as_view(), name="dds"),
    #  FILTERED DDS BY PRIMARY KEY
    path('dds/<int:id>', DDSApiView.as_view(), name="ddsFilter"),

    # GET ALL SSM RANDOM ORDER IN DB
    # path('ssmrandom/', SSMRandomOrderApiView.as_view(), name="ssmrandom"),
    # # GET FILTERED SSM RANDOM ORDER BY PRIMARY KEY
    # path('ssmrandom/<int:id>', SSMRandomOrderApiView.as_view(), name="ssmrandomFilter"),

    # GET ALL PATROL QUESTS IN DB
    path('patrolquests/', PatrolQuestApiView.as_view(), name="patrolquests"),
    #  FILTERED PATROL QUEST BY PRIMARY KEY
    path('patrolquests/<int:id>', PatrolQuestApiView.as_view(), name="patrolquestsFilter"),

    #  ALL PATROL WEEKS IN DB
    path('patrolweeks/', PatrolWeekApiView.as_view(), name="patrolweeks"),
    #  FILTERED PATROL WEEK BY PRIMARY KEY
    path('patrolweeks/<int:id>', PatrolWeekApiView.as_view(), name="patrolweeksFilter"),

    #  ALL POSSIBLE ANSWERS IN DB
    path('possibleanswers/', PossibleAnswerApiView.as_view(), name="possibleanswers"),
    #  FILTERED POSSIBLE ANSWER BY PRIMARY KEY
    path('possibleanswers/<int:id>', PossibleAnswerApiView.as_view(), name="possibleanswersFilter"),

    #  ALL PATROL ANSWERS IN DB
    path('patrolanswers/', PatrolAnswerApiView.as_view(), name="patrolanswers"),
    #  FILTERED PATROL ANSWER BY PRIMARY KEY
    path('patrolanswers/<int:id>', PatrolAnswerApiView.as_view(), name="patrolanswersFilter"),

    path('locations/', LocationApiView.as_view(), name="locations"),
    # FILTERED LOCATION BY PRIMARY KEY
    path('locations/<int:id>', LocationApiView.as_view(), name="locationsFilter"),

    #  ALL EVENTS IN DB
    path('events/', EventApiView.as_view(), name="events"),
    #  FILTERED EVENTS BY PRIMARY KEY
    path('events/<int:id>', EventApiView.as_view(), name="eventsFilter"),
    
    # ALL TEAM EVENTS IN DB
    path('teamevents/', TeamEventApiView.as_view(), name="teamEvents"),
    # FILTERED TEAM EVENT BY PRIMARY KEY
    path('teamevents/<int:id>', TeamEventApiView.as_view(), name="teamEventsFilter"),
    # #  ALL PROJECTS IN DB
    # path('projects/', ProjectApiView.as_view(), name="projects"),
    # #  FILTERED PROJECT BY PRIMARY KEY
    # path('projects/<int:id>', ProjectApiView.as_view(), name="projectsFilter"),

    # #  ALL SCHEDULE LOCATIONS IN DB
    # path('schedulelocations/', LocationScheduleApiView.as_view(), name="schedulelocations"),
    # #  FILTERED SCHEDULE LOCATION BY PRIMARY KEY
    # path('schedulelocations/<int:id>', LocationScheduleApiView.as_view(), name="schedulelocationsFilter"),

    # #  ALL SCHEDULE EVENTS IN DB
    # path('scheduleevents/', ScheduleEventApiView.as_view(), name="scheduleevents"),
    # #  FILTERED SCHEDULE EVENT BY PRIMARY KEY
    # path('scheduleevents/<int:id>', ScheduleEventApiView.as_view(), name="scheduleeventsFilter"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)