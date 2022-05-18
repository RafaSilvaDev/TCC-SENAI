from asyncio.windows_events import NULL
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .paginations import *
from rest_framework import filters
from rest_framework import generics
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
from tempfile import *
from subprocess import Popen, PIPE
from django.http import HttpResponse
from ERP_BACKEND.settings import BASE_DIR
from drf_pdf.response import PDFFileResponse
from drf_pdf.renderer import PDFRenderer
from rest_framework import status
# Create your views here.

giantPag = ResponsePaginationGiant()
class search_view_dds(generics.ListCreateAPIView):
    search_fields = ['title', 'frontText', 'backText']
    filter_backends = (filters.SearchFilter,)
    queryset = DDS.objects.all()
    serializer_class = DDSSerializer

class search_view_ssm(generics.ListCreateAPIView):
    search_fields = ['fk_type__type']
    filter_backends = (filters.SearchFilter,)
    queryset = SSM.objects.all()
    serializer_class = SSMSerializer


class filter_view_ssm(generics.ListCreateAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = SSM.objects.all()
    serializer_class = SSMSerializer
    

class fetchpdf(APIView):
    renderer_classes = (PDFRenderer, )

    def get(self, request):
        return PDFFileResponse(
            file_path='/path/to/file.pdf',
            status=status.HTTP_200_OK
        )

class PlantApiView(APIView):
    """
    API Plant
    """

    
    #permission_classes = (IsAuthenticated,)   
    def get(self, request, id=NULL):
        self.plant = ''
        context = {'request': request}
        if id is NULL:
            plant = Plant.objects.all()
            results = giantPag.paginate_queryset(plant, request)
            serializer = PlantSerializer(results, many=True, context=context)
            return giantPag.get_paginated_response(serializer.data)
        else:
            try:
                self.plant = Plant.objects.get(id=id)
                self.serializer = PlantSerializer(self.plant)
            except Plant.DoesNotExist:
                return Response({
                    'msg': 'Plant Not Found' if self.plant == '' else 'Error',
                    'status': 404,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,
                })
        return Response(self.serializer.data)

    def post(self, request):
        context = {'request': request}
        self.plant = ''
        self.serializer = PlantSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data inserted was: {Plant.objects.latest('id')}",
            'status': 200,
            'url': request.path,
            'user': request.user.username,
            'method': request.method,
        })
    
    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                plant = Plant.objects.get(id=id)
                plant.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

    def put(self, request, id=NULL):
        
        self.response = {}
        try:
            if id is not NULL:
                plant = Plant.objects.get(id=id)
                serializer = PlantSerializer(plant, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                self.response = {
                    'msg': f"The data updated was: {plant.id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the UPDATE method",
                    'status': 500,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

class AreaApiView(APIView):
    """
    API Area
    """
    def get(self, request, id=NULL):
        self.area = ''
        context = {'request': request}
        if id is NULL:
            area = Area.objects.all()
            results = giantPag.paginate_queryset(area, request)
            serializer = AreaSerializer(results, many=True, context=context)
            return giantPag.get_paginated_response(serializer.data)
        else:
            try:
                self.area = Area.objects.get(id=id)
                self.serializer = AreaSerializer(self.area)
            except Area.DoesNotExist:
                return Response({
                    'msg': 'Area Not Found' if self.area == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)

    def post(self, request):
        context = {'request': request}
        self.area = ''
        self.serializer = AreaSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {Area.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })
    
    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                area = Area.objects.get(id=id)
                area.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

    def put(self, request, id=NULL):
        
        self.response = {}
        try:
            if id is not NULL:
                area = Area.objects.get(id=id)
                serializer = AreaSerializer(area, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                self.response = {
                    'msg': f"The data updated was: {area.id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the UPDATE method",
                    'status': 500,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

class TeamApiView(APIView):
    """
    API Team
    """
    def get(self, request, id=NULL):
        self.team = ''
        context = {'request': request}
        if id is NULL:
            team = Team.objects.all()
            results = giantPag.paginate_queryset(team, request)
            serializer = AreaSerializer(results, many=True, context=context)
            return giantPag.get_paginated_response(serializer.data)
        else:
            try:
                self.team = Team.objects.get(id=id)
                self.serializer = TeamSerializer(self.team)
            except Team.DoesNotExist:
                return Response({
                    'msg': 'Team Not Found' if self.team == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)

    def post(self, request):
        context = {'request': request}
        self.team = ''
        self.serializer = TeamSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {Team.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })
    
    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                area = Team.objects.get(id=id)
                area.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

    def put(self, request, id=NULL):
        
        self.response = {}
        try:
            if id is not NULL:
                area = Team.objects.get(id=id)
                serializer = AreaSerializer(area, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                self.response = {
                    'msg': f"The data updated was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the UPDATE method",
                    'status': 500,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)   

class ProfileServiceApiView(APIView):
    """
    API Profile Service
    """
    def get(self, request, id=NULL):
        self.profile_service = ''
        context = {'request': request}
        if id is NULL:
            profile_service = ProfileService.objects.all()
            results = giantPag.paginate_queryset(profile_service, request)
            serializer = ProfileServiceSerializer(results, many=True, context=context)
            return giantPag.get_paginated_response(serializer.data)
        else:
            try:
                self.profile_service = ProfileService.objects.get(id=id)
                self.serializer = ProfileServiceSerializer(self.profile_service)
            except ProfileService.DoesNotExist:
                return Response({
                    'msg': 'Profile Service Not Found' if self.profile_service == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)

    def post(self, request):
        context = {'request': request}
        self.profile_service = ''
        self.serializer = ProfileServiceSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {ProfileService.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })

    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                profile = ProfileService.objects.get(id=id)
                profile.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

    def put(self, request, id=NULL):
            
            self.response = {}
            try:
                if id is not NULL:
                    profile = ProfileService.objects.get(id=id)
                    serializer = ProfileServiceSerializer(profile, data=request.data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    self.response = {
                        'msg': f"The data updated was: {profile.id}",
                        'status': 200,
                        'url': request.path,
                        'user': request.user.username,
                        'method': request.method,}
                else:
                    self.response = {
                        'msg': "No ID were informed to the UPDATE method",
                        'status': 500,
                        'url' : request.path,
                        'user': request.user.username,
                        'method': request.method,}
            except:
                self.response = {
                    'msg': 'Something went wrong - Check the values or try again later',
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
            return Response(self.response)

class AccessLevelApiView(APIView):
    """
    API Access Level
    """
    def get(self, request, id=NULL):
        self.access_level = ''
        context = {'request': request}
        if id is NULL:
            access_level = AccessLevel.objects.all()
            results = giantPag.paginate_queryset(access_level, request)
            serializer = AccessLevelSerializer(results, many=True, context=context)
            return giantPag.get_paginated_response(serializer.data)
        else:
            try:
                self.access_level = AccessLevel.objects.get(id=id)
                self.serializer = AccessLevelSerializer(self.access_level)
            except AccessLevel.DoesNotExist:
                return Response({
                    'msg': 'Access Level Not Found' if self.access_level == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)

    def post(self, request):
        context = {'request': request}
        self.access_level = ''
        self.serializer = AccessLevelSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {AccessLevel.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })

    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                access = AccessLevel.objects.get(id=id)
                access.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)
    
    def put(self, request, id=NULL):
            
            self.response = {}
            try:
                if id is not NULL:
                    access = AccessLevel.objects.get(id=id)
                    serializer = AccessLevelSerializer(access, data=request.data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    self.response = {
                        'msg': f"The data updated was: {access.id}",
                        'status': 200,
                        'url': request.path,
                        'user': request.user.username,
                        'method': request.method,}
                else:
                    self.response = {
                        'msg': "No ID were informed to the UPDATE method",
                        'status': 500,
                        'url' : request.path,
                        'user': request.user.username,
                        'method': request.method,}
            except:
                self.response = {
                    'msg': 'Something went wrong - Check the values or try again later',
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
            return Response(self.response)

class SimpleUserApiView(APIView):
    """
    API Simple User
    """
    def get(self, request, id=NULL):
        self.simple_user = ''
        context = {'request': request}
        if id is NULL:
            simple_user = SimpleUser.objects.all()
            results = giantPag.paginate_queryset(simple_user, request)
            serializer = SimpleUserSerializer(results, many=True, context=context)
            return giantPag.get_paginated_response(serializer.data)
        else:
            try:
                self.simple_user = SimpleUser.objects.get(id=id)
                self.serializer = SimpleUserSerializer(self.simple_user)
            except SimpleUser.DoesNotExist:
                return Response({
                    'msg': 'Simple User Not Found' if self.simple_user == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)

    def post(self, request):
        context = {'request': request}
        self.simple_user = ''
        self.serializer = SimpleUserSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {SimpleUser.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })

    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                user = SimpleUser.objects.get(id=id)
                user.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)
    
    def put(self, request, id=NULL):
            
            self.response = {}
            try:
                if id is not NULL:
                    user = SimpleUser.objects.get(id=id)
                    serializer = SimpleUserSerializer(user, data=request.data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    self.response = {
                        'msg': f"The data updated was: {user.id}",
                        'status': 200,
                        'url': request.path,
                        'user': request.user.username,
                        'method': request.method,}
                else:
                    self.response = {
                        'msg': "No ID were informed to the UPDATE method",
                        'status': 500,
                        'url' : request.path,
                        'user': request.user.username,
                        'method': request.method,}
            except:
                self.response = {
                    'msg': 'Something went wrong - Check the values or try again later',
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
            return Response(self.response)

class SystemApiView(APIView):
    """
    API System
    """
    def get(self, request, id=NULL):
        self.system = ''
        context = {'request': request}
        if id is NULL:
            system = System.objects.all()
            results = giantPag.paginate_queryset(system, request)
            serializer = SystemSerializer(results, many=True, context=context)
            return giantPag.get_paginated_response(serializer.data)
        else:
            try:
                self.system = System.objects.get(id=id)
                self.serializer = SystemSerializer(self.system)
            except System.DoesNotExist:
                return Response({
                    'msg': 'System Not Found' if self.system == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)

    def post(self, request):
        context = {'request': request}
        self.system = ''
        self.serializer = SystemSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {System.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })

    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                system = System.objects.get(id=id)
                system.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)
    
    def put(self, request, id=NULL):
            
            self.response = {}
            try:
                if id is not NULL:
                    system = System.objects.get(id=id)
                    serializer = SystemSerializer(system, data=request.data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    self.response = {
                        'msg': f"The data updated was: {system.id}",
                        'status': 200,
                        'url': request.path,
                        'user': request.user.username,
                        'method': request.method,}
                else:
                    self.response = {
                        'msg': "No ID were informed to the UPDATE method",
                        'status': 500,
                        'url' : request.path,
                        'user': request.user.username,
                        'method': request.method,}
            except:
                self.response = {
                    'msg': 'Something went wrong - Check the values or try again later',
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
            return Response(self.response)

class LocationApiView(APIView):
    def get(self, request, id=NULL):
        self.location = ''
        context = {'request': request}
        if id is NULL:
            location = Location.objects.all()
            results = giantPag.paginate_queryset(location, request)
            serializer = LocationSerializer(results, many=True, context=context)
            return giantPag.get_paginated_response(serializer.data)
        else:
            try:
                self.location = Location.objects.get(id=id)
                self.serializer = LocationSerializer(self.location)
            except Location.DoesNotExist:
                return Response({
                    'msg': 'Location Not Found' if self.location == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)
    
    def post(self, request):
        self.location = ''
        self.serializer = LocationSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {Location.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })

    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                location = Location.objects.get(id=id)
                location.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,
                }
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,
                }
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

    def put(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                location = Location.objects.get(id=id)
                serializer = LocationSerializer(location, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                self.response = {
                    'msg': f"The data updated was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the UPDATE method",
                    'status': 500,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response) 


class EventApiView(APIView):
    def get(self, request, id=NULL):
        self.event = ''
        context = {'request': request}
        if id is NULL:
            event = Event.objects.all()
            results = giantPag.paginate_queryset(event, request)
            serializer = EventSerializer(results, many=True, context=context)
            return giantPag.get_paginated_response(serializer.data)
        else:
            try:
                self.event = Event.objects.get(id=id)
                self.serializer = EventSerializer(self.event)
            except Location.DoesNotExist:
                return Response({
                    'msg': 'Event Not Found' if self.event == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)
    
    def post(self, request):
        self.event = ''
        self.serializer = EventSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {Event.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })

    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                event = Event.objects.get(id=id)
                event.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,
                }
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,
                }
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

    def put(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                event = Event.objects.get(id=id)
                serializer = EventSerializer(event, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                self.response = {
                    'msg': f"The data updated was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the UPDATE method",
                    'status': 500,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response) 

class TeamEventApiView(APIView):
    def get(self, request, id=NULL):
        self.event = ''
        context = {'request': request}
        if id is NULL:
            teamEvent = TeamEvent.objects.all()
            results = giantPag.paginate_queryset(teamEvent, request)
            serializer = TeamEventSerializer(results, many=True, context=context)
            return giantPag.get_paginated_response(serializer.data)
        else:
            try:
                self.teamEvent = Event.objects.get(id=id)
                self.serializer = TeamEventSerializer(self.teamEvent)
            except TeamEvent.DoesNotExist:
                return Response({
                    'msg': 'Team Even Not Found' if self.teamEvent == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)
    
    def post(self, request):
        self.teamEvent = ''
        self.serializer = TeamEventSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {TeamEvent.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })

    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                teamEvent = TeamEvent.objects.get(id=id)
                teamEvent.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,
                }
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,
                }
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

    def put(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                teamEvent = TeamEvent.objects.get(id=id)
                serializer = TeamEventSerializer(teamEvent, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                self.response = {
                    'msg': f"The data updated was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the UPDATE method",
                    'status': 500,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response) 

# class Colab_TeamApiView(APIView):

#     def get(self, request, id=NULL):
#         self.colab_team = ''
#         context = {'request': request}
#         if id is NULL:
#             colab_team = Colab_Team.objects.all()
#             results = giantPag.paginate_queryset(colab_team, request)
#             serializer = Colab_TeamSerializer(results, many=True, context=context)
#             return giantPag.get_paginated_response(serializer.data)
#         else:
#             try:
#                 self.colab_team = SSMType.objects.get(id=id)
#                 self.serializer = SSMTypeSerializer(self.colab_team)
#             except SSMType.DoesNotExist:
#                 return Response({
#                     'msg': 'SSM Type Not Found' if self.colab_team == '' else 'Error',
#                     'status': 404,
#                     'url': request.path
#                 })
#         return Response(self.serializer.data)
class SSMTypeApiView(APIView):
    """
    API SSM Type
    """
    def get(self, request, id=NULL):
        self.ssm_type = ''
        context = {'request': request}
        if id is NULL:
            
            ssm_type = SSMType.objects.all()
            results = giantPag.paginate_queryset(ssm_type, request)
            serializer = SSMTypeSerializer(results, many=True, context=context)
            return giantPag.get_paginated_response(serializer.data)
        else:
            try:
                self.ssm_type = SSMType.objects.get(id=id)
                self.serializer = SSMTypeSerializer(self.ssm_type)
            except SSMType.DoesNotExist:
                return Response({
                    'msg': 'SSM Type Not Found' if self.ssm_type == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)

    def post(self, request):
        context = {'request': request}
        self.ssm_type = ''
        self.serializer = SSMTypeSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {SSMType.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })

    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                ssm_type = SSMType.objects.get(id=id)
                ssm_type.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

    def put(self, request, id=NULL):
            
            self.response = {}
            try:
                if id is not NULL:
                    ssm_type = SSMType.objects.get(id=id)
                    serializer = SSMTypeSerializer(ssm_type, data=request.data)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
                    self.response = {
                        'msg': f"The data updated was: {ssm_type.id}",
                        'status': 200,
                        'url': request.path,
                        'user': request.user.username,
                        'method': request.method,}
                else:
                    self.response = {
                        'msg': "No ID were informed to the UPDATE method",
                        'status': 500,
                        'url' : request.path,
                        'user': request.user.username,
                        'method': request.method,}
            except:
                self.response = {
                    'msg': 'Something went wrong - Check the values or try again later',
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
            return Response(self.response)

class SSMApiView(APIView):
    """
    API SSM
    """
    def get(self, request, id=NULL):
        
        
        self.ssm = ''
        context = {'request': request}
        if id is NULL:
            
            ssm = SSM.objects.all()
            results = giantPag.paginate_queryset(ssm, request)
            serializer = SSMSerializer(results, many=True, context=context)
            return giantPag.get_paginated_response(serializer.data)
        else:
            try:
                self.ssm = SSM.objects.get(id=id)
                self.serializer = SSMSerializer(self.ssm)
            except SSM.DoesNotExist:
                return Response({
                    'msg': 'SSM Not Found' if self.ssm == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)

    def post(self, request):
        context = {'request': request}
        self.ssm = ''
        self.serializer = SSMSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {SSM.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })

    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                ssm = SSM.objects.get(id=id)
                ssm.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)
    
    def put(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                ssm = SSM.objects.get(id=id)
                serializer = SSMSerializer(ssm, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                self.response = {
                    'msg': f"The data updated was: {ssm.id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the UPDATE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

class DDSApiView(APIView):
    """
    API DDS
    """

    def get(self, request, id=NULL):
        self.dds = ''
        context = {'request': request}
        if id is NULL:
            ssm_resp = DDS.objects.filter(fk_type = request.GET['type']) if 'type' in request.GET else DDS.objects.all() 
            paginator = ResponsePaginationMedium()
            results = paginator.paginate_queryset(ssm_resp, request)
            serializer = DDSSerializer(results, many=True, context=context)
            return paginator.get_paginated_response(serializer.data)
        else:
            try:
                self.ssm = DDS.objects.get(id=id)
                self.serializer = DDSSerializer(self.ssm)
            except DDS.DoesNotExist:
                return Response({
                    'msg': 'DDS Not Found' if self.ssm == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)

    def post(self, request):
        context = {'request': request}
        self.ssm = ''
        self.serializer = DDSSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {DDS.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })

    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                ssm = DDS.objects.get(id=id)
                ssm.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

    def put(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                ssm = DDS.objects.get(id=id)
                serializer = DDSSerializer(ssm, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                self.response = {
                    'msg': f"The data updated was: {ssm.id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the UPDATE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

# class SSMRandomOrderApiView(APIView):
#     """
#     API SSM Random Order
#     """
#     def get(self, request, id=NULL):
#         context = {'request': request}
#         if id is NULL:
#             ssm_random_order = SSMRandomOrder.objects.all()
#             results = giantPag.paginate_queryset(ssm_random_order, request)
#             serializer = SSMRandomOrderSerializer(results, many=True, context=context)
#             return giantPag.get_paginated_response(serializer.data)
#         else:
#             try:
#                 self.ssm_random_order = SSMRandomOrder.objects.get(id=id)
#                 self.serializer = SSMRandomOrderSerializer(self.ssm_random_order)
#             except SSMRandomOrder.DoesNotExist:
#                 return Response({
#                     'msg': 'SSM Random Order Not Found' if self.ssm_random_order == '' else 'Error',
#                     'status': 404,
#                     'url': request.path
#                 })
#         return Response(self.serializer.data)

#     def post(self, request):
#         context = {'request': request}
#         self.ssm_random_order = ''
#         self.serializer = SSMRandomOrderSerializer(data=request.data, many=True)
#         self.serializer.is_valid(raise_exception=True)
#         self.serializer.save()
#         return Response({
#             'msg': f"The data was inserted - id: {SSMRandomOrder.objects.latest('id')}",
#             'status': 200,
#             'url': request.path
#         })

#     def delete(self, request, id=NULL):
#         self.response = {}
#         try:
#             if id is not NULL:
#                 ssm_random_order = SSMRandomOrder.objects.get(id=id)
#                 ssm_random_order.delete()
#                 self.response = {
#                     'msg': f"The data deleted was: {id}",
#                     'status': 200,
#                     'url': request.path,
#                     'user': request.user.username,
#                     'method': request.method,}
#             else:
#                 self.response = {
#                     'msg': "No ID were informed to the DELETE method",
#                     'status': 500,
#                     'url' : request.path,
#                     'user': request.user.username
#                 }
#         except:
#             self.response = {
#                 'msg': 'Something went wrong - Check the values or try again later',
#                 'status': 500,
#                 'url' : request.path,
#                 'user': request.user.username
#             }
#         return Response(self.response)

#     def put(self, request, id=NULL):
#         self.response = {}
#         try:
#             if id is not NULL:
#                 ssm_random_order = SSMRandomOrder.objects.get(id=id)
#                 serializer = SSMRandomOrderSerializer(ssm_random_order, data=request.data)
#                 serializer.is_valid(raise_exception=True)
#                 serializer.save()
#                 self.response = {
#                     'msg': f"The data updated was: {ssm_random_order.id}",
#                     'status': 200,
#                     'url': request.path,
#                     'user': request.user.username,
#                     'method': request.method,}
#             else:
#                 self.response = {
#                     'msg': "No ID were informed to the UPDATE method",
#                     'status': 500,
#                     'url' : request.path,
#                     'user': request.user.username,
#                     'method': request.method,}
#         except:
#             self.response = {
#                 'msg': 'Something went wrong - Check the values or try again later',
#                 'status': 500,
#                 'url' : request.path,
#                 'user': request.user.username
#             }
#         return Response(self.response)

class PatrolQuestApiView(APIView):
    """
    API Patrol Quest
    """
    def get(self, request, id=NULL):
        self.patrol_quest = ''
        context = {'request': request}
        if id is NULL:
            patrol_quest = PatrolQuest.objects.all()
            results = giantPag.paginate_queryset(patrol_quest, request)
            serializer = PatrolQuestSerializer(results, many=True, context=context)
            return giantPag.get_paginated_response(serializer.data)
        else:
            try:
                self.patrol_quest = PatrolQuest.objects.get(id=id)
                self.serializer = PatrolQuestSerializer(self.patrol_quest)
            except PatrolQuest.DoesNotExist:
                return Response({
                    'msg': 'Patrol Quest Not Found' if self.patrol_quest == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)

    def post(self, request):
        context = {'request': request}
        self.patrol_quest = ''
        self.serializer = PatrolQuestSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {PatrolQuest.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })

    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                patrol_quest = PatrolQuest.objects.get(id=id)
                patrol_quest.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)
    
    def put(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                patrol_quest = PatrolQuest.objects.get(id=id)
                serializer = PatrolQuestSerializer(patrol_quest, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                self.response = {
                    'msg': f"The data updated was: {patrol_quest.id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the UPDATE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

class PatrolWeekApiView(APIView):
    """
    API Patrol Week
    """
    def get(self, request, id=NULL):
        self.patrol_week = ''
        context = {'request': request}
        if id is NULL:
            self.patrol_week = PatrolWeek.objects.all()
            self.serializer = PatrolWeekSerializer(self.patrol_week, many=True, context=context)
        else:
            try:
                self.patrol_week = PatrolWeek.objects.get(id=id)
                self.serializer = PatrolWeekSerializer(self.patrol_week)
            except PatrolWeek.DoesNotExist:
                return Response({
                    'msg': 'Patrol Week Not Found' if self.patrol_week == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)

    def post(self, request):
        context = {'request': request}
        self.patrol_week = ''
        self.serializer = PatrolWeekSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {PatrolWeek.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })

    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                patrol_week = PatrolWeek.objects.get(id=id)
                patrol_week.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

    def put(self, request, id=NULL):
        self.response={}
        try:
            if id is not NULL:
                patrol_week = PatrolWeek.objects.get(id=id)
                serializer = PatrolWeekSerializer(patrol_week, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                self.response = {
                    'msg': f"The data updated was: {patrol_week.id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the UPDATE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

class PossibleAnswerApiView(APIView):
    """
    API Possible Answer
    """
    def get(self, request, id=NULL):
        self.possible_answer = ''
        context = {'request': request}
        if id is NULL:
            self.possible_answer = PossibleAnswer.objects.all()
            self.serializer = PossibleAnswerSerializer(self.possible_answer, many=True, context=context)
        else:
            try:
                self.possible_answer = PossibleAnswer.objects.get(id=id)
                self.serializer = PossibleAnswerSerializer(self.possible_answer)
            except PossibleAnswer.DoesNotExist:
                return Response({
                    'msg': 'Possible Answer Not Found' if self.possible_answer == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)

    def post(self, request):
        context = {'request': request}
        self.possible_answer = ''
        self.serializer = PossibleAnswerSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {PossibleAnswer.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })

    def delete(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                possible_answer = PossibleAnswer.objects.get(id=id)
                possible_answer.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)
    
    def put(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                possible_answer = PossibleAnswer.objects.get(id=id)
                serializer = PossibleAnswerSerializer(possible_answer, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                self.response = {
                    'msg': f"The data updated was: {possible_answer.id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the UPDATE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)

class PatrolAnswerApiView(APIView):
    """
    API Patrol Answer
    """
    def get(self, request, id=NULL):
        self.patrol_answer = ''
        context = {'request': request}
        if id is NULL:
            self.patrol_answer = PatrolAnswer.objects.all()
            self.serializer = PatrolAnswerSerializer(self.patrol_answer, many=True, context=context)
        else:
            try:
                self.patrol_answer = PatrolAnswer.objects.get(id=id)
                self.serializer = PatrolAnswerSerializer(self.patrol_answer)
            except PatrolAnswer.DoesNotExist:
                return Response({
                    'msg': 'Patrol Answer Not Found' if self.patrol_answer == '' else 'Error',
                    'status': 404,
                    'url': request.path
                })
        return Response(self.serializer.data)

    def post(self, request):
        context = {'request': request}
       
        self.serializer = PatrolAnswerSerializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.save()
        return Response({
            'msg': f"The data was inserted - id: {PatrolAnswer.objects.latest('id')}",
            'status': 200,
            'url': request.path
        })

    def delete(self, request, id=NULL):
        self.response={}
        try:
            if id is not NULL:
                patrol_answer = PatrolAnswer.objects.get(id=id)
                patrol_answer.delete()
                self.response = {
                    'msg': f"The data deleted was: {id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the DELETE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username
                }
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)
    
    def put(self, request, id=NULL):
        self.response = {}
        try:
            if id is not NULL:
                patrol_answer = PatrolAnswer.objects.get(id=id)
                serializer = PatrolAnswerSerializer(patrol_answer, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                self.response = {
                    'msg': f"The data updated was: {patrol_answer.id}",
                    'status': 200,
                    'url': request.path,
                    'user': request.user.username,
                    'method': request.method,}
            else:
                self.response = {
                    'msg': "No ID were informed to the UPDATE method",
                    'status': 500,
                    'url' : request.path,
                    'user': request.user.username,
                    'method': request.method,}
        except:
            self.response = {
                'msg': 'Something went wrong - Check the values or try again later',
                'status': 500,
                'url' : request.path,
                'user': request.user.username
            }
        return Response(self.response)


# class ProjectApiView(APIView):
#     """
#     API Project
#     """
#     def get(self, request, id=NULL):
#         self.project = ''
#         context = {'request': request}
#         if id is NULL:
#             self.project = Project.objects.all()
#             self.serializer = ProjectSerializer(self.project, many=True, context=context)
#         else:
#             try:
#                 self.project = Project.objects.get(id=id)
#                 self.serializer = ProjectSerializer(self.project)
#             except Project.DoesNotExist:
#                 return Response({
#                     'msg': 'Project Not Found' if self.project == '' else 'Error',
#                     'status': 404,
#                     'url': request.path
#                 })
#         return Response(self.serializer.data)

#     def post(self, request):
#         context = {'request': request}
#         self.project = ''
#         self.serializer = ProjectSerializer(data=request.data, many=True)
#         self.serializer.is_valid(raise_exception=True)
#         self.serializer.save()
#         return Response({
#             'msg': f"The data was inserted - id: {Project.objects.latest('id')}",
#             'status': 200,
#             'url': request.path
#         })

#     def delete(self, request, id=NULL):
#         self.response={}
#         try:
#             if id is not NULL:
#                 project = Project.objects.get(id=id)
#                 project.delete()
#                 self.response = {
#                     'msg': f"The data deleted was: {id}",
#                     'status': 200,
#                     'url': request.path,
#                     'user': request.user.username,
#                     'method': request.method,}
#             else:
#                 self.response = {
#                     'msg': "No ID were informed to the DELETE method",
#                     'status': 500,
#                     'url' : request.path,
#                     'user': request.user.username
#                 }
#         except:
#             self.response = {
#                 'msg': 'Something went wrong - Check the values or try again later',
#                 'status': 500,
#                 'url' : request.path,
#                 'user': request.user.username
#             }
#         return Response(self.response)
    
#     def put(self, request, id=NULL):
#         self.response = {}
#         try:
#             if id is not NULL:
#                 project = Project.objects.get(id=id)
#                 serializer = ProjectSerializer(project, data=request.data)
#                 serializer.is_valid(raise_exception=True)
#                 serializer.save()
#                 self.response = {
#                     'msg': f"The data updated was: {project.id}",
#                     'status': 200,
#                     'url': request.path,
#                     'user': request.user.username,
#                     'method': request.method,}
#             else:
#                 self.response = {
#                     'msg': "No ID were informed to the UPDATE method",
#                     'status': 500,
#                     'url' : request.path,
#                     'user': request.user.username,
#                     'method': request.method,}
#         except:
#             self.response = {
#                 'msg': 'Something went wrong - Check the values or try again later',
#                 'status': 500,
#                 'url' : request.path,
#                 'user': request.user.username
#             }
#         return Response(self.response)

# class LocationScheduleApiView(APIView):
#     """
#     API Location Schedule
#     """
#     def get(self, request, id=NULL):
#         self.location_schedule = ''
#         context = {'request': request}
#         if id is NULL:
#             self.location_schedule = LocationSchedule.objects.all()
#             self.serializer = LocationScheduleSerializer(self.location_schedule, many=True, context=context)
#         else:
#             try:
#                 self.location_schedule = LocationSchedule.objects.get(id=id)
#                 self.serializer = LocationScheduleSerializer(self.location_schedule)
#             except LocationSchedule.DoesNotExist:
#                 return Response({
#                     'msg': 'Location Schedule Not Found' if self.location_schedule == '' else 'Error',
#                     'status': 404,
#                     'url': request.path
#                 })
#         return Response(self.serializer.data)

#     def post(self, request):
#         context = {'request': request}
#         self.location_schedule = ''
#         self.serializer = LocationScheduleSerializer(data=request.data, many=True)
#         self.serializer.is_valid(raise_exception=True)
#         self.serializer.save()
#         return Response({
#             'msg': f"The data was inserted - id: {LocationSchedule.objects.latest('id')}",
#             'status': 200,
#             'url': request.path
#         })
    
#     def delete(self, request, id=NULL):
#         self.response={}
#         try:
#             if id is not NULL:
#                 location_schedule = LocationSchedule.objects.get(id=id)
#                 location_schedule.delete()
#                 self.response = {
#                     'msg': f"The data deleted was: {id}",
#                     'status': 200,
#                     'url': request.path,
#                     'user': request.user.username,
#                     'method': request.method,}
#             else:
#                 self.response = {
#                     'msg': "No ID were informed to the DELETE method",
#                     'status': 500,
#                     'url' : request.path,
#                     'user': request.user.username
#                 }
#         except:
#             self.response = {
#                 'msg': 'Something went wrong - Check the values or try again later',
#                 'status': 500,
#                 'url' : request.path,
#                 'user': request.user.username
#             }
#         return Response(self.response)
    
#     def put(self, request, id=NULL):
#         self.response = {}
#         try:
#             if id is not NULL:
#                 location_schedule = LocationSchedule.objects.get(id=id)
#                 serializer = LocationScheduleSerializer(location_schedule, data=request.data)
#                 serializer.is_valid(raise_exception=True)
#                 serializer.save()
#                 self.response = {
#                     'msg': f"The data updated was: {location_schedule.id}",
#                     'status': 200,
#                     'url': request.path,
#                     'user': request.user.username,
#                     'method': request.method,}
#             else:
#                 self.response = {
#                     'msg': "No ID were informed to the UPDATE method",
#                     'status': 500,
#                     'url' : request.path,
#                     'user': request.user.username,
#                     'method': request.method,}
#         except:
#             self.response = {
#                 'msg': 'Something went wrong - Check the values or try again later',
#                 'status': 500,
#                 'url' : request.path,
#                 'user': request.user.username
#             }
#         return Response(self.response)

# class ScheduleEventApiView(APIView):
#     """
#     API Schedule Event
#     """
#     def get(self, request, id=NULL):
#         self.schedule_event = ''
#         context = {'request': request}
#         if id is NULL:
#             self.schedule_event = ScheduleEvent.objects.all()
#             self.serializer = ScheduleEventSerializer(self.schedule_event, many=True, context=context)
#         else:
#             try:
#                 self.schedule_event = ScheduleEvent.objects.get(id=id)
#                 self.serializer = ScheduleEventSerializer(self.schedule_event)
#             except ScheduleEvent.DoesNotExist:
#                 return Response({
#                     'msg': 'Schedule Event Not Found' if self.schedule_event == '' else 'Error',
#                     'status': 404,
#                     'url': request.path
#                 })
#         return Response(self.serializer.data)

#     def post(self, request):
#         context = {'request': request}
#         self.schedule_event = ''
#         self.serializer = ScheduleEventSerializer(data=request.data, many=True)
#         self.serializer.is_valid(raise_exception=True)
#         self.serializer.save()
#         return Response({
#             'msg': f"The data was inserted - id: {ScheduleEvent.objects.latest('id')}",
#             'status': 200,
#             'url': request.path
#         })

#     def delete(self, request, id=NULL):
#         self.response={}
#         try:
#             if id is not NULL:
#                 schedule_event = ScheduleEvent.objects.get(id=id)
#                 schedule_event.delete()
#                 self.response = {
#                     'msg': f"The data deleted was: {id}",
#                     'status': 200,
#                     'url': request.path,
#                     'user': request.user.username,
#                     'method': request.method,}
#             else:
#                 self.response = {
#                     'msg': "No ID were informed to the DELETE method",
#                     'status': 500,
#                     'url' : request.path,
#                     'user': request.user.username
#                 }
#         except:
#             self.response = {
#                 'msg': 'Something went wrong - Check the values or try again later',
#                 'status': 500,
#                 'url' : request.path,
#                 'user': request.user.username
#             }
#         return Response(self.response)
    
#     def put(self, request, id=NULL):
#         self.response = {}
#         try:
#             if id is not NULL:
#                 schedule_event = ScheduleEvent.objects.get(id=id)
#                 serializer = ScheduleEventSerializer(schedule_event, data=request.data)
#                 serializer.is_valid(raise_exception=True)
#                 serializer.save()
#                 self.response = {
#                     'msg': f"The data updated was: {schedule_event.id}",
#                     'status': 200,
#                     'url': request.path,
#                     'user': request.user.username,
#                     'method': request.method,}
#             else:
#                 self.response = {
#                     'msg': "No ID were informed to the UPDATE method",
#                     'status': 500,
#                     'url' : request.path,
#                     'user': request.user.username,
#                     'method': request.method,}
#         except:
#             self.response = {
#                 'msg': 'Something went wrong - Check the values or try again later',
#                 'status': 500,
#                 'url' : request.path,
#                 'user': request.user.username
#             }
        return Response(self.response)


class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer