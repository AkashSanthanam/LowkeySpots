from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import mapRequest, mapSerializer, getMap
from .models import USER, USER_RELATION
from rest_framework import status
from utils import create_token, hash_password, verify_password
from friendManager.serializers import getUser
from utils import token_to_user, error_returner
from .models import MAP_USER, MAP
from django.core.exceptions import ValidationError
import os
from django.core.exceptions import ObjectDoesNotExist
from typing import Callable
from django.conf import settings 
from friendManager.views import userEquals
from markerManager.serializers import imageSerializer
import shutil
# Create your views here.

@api_view(['POST'])
def makeMap(request: Response) -> Response:
    #authenticate user:
    user=userEquals(request)
    if user is None: return Response(status=408)
    
    #make sure its a valid map request
    mapObject = mapSerializer(data=request.data)
    if mapObject.is_valid() is False:
        return Response(status=500)
    mapObject = mapObject.save()
    
    #make map user with map number
    mapUserInstance = MAP_USER(mapId=mapObject, userId=user, status=0)
    mapUserInstance.save()
    
    #show a 3 level higher
    
    #join the path to correct path from lowkeySpots/
    directory_path = os.path.join(settings.ROOT_FOLDER, "frontEnd/map-app/react-app/src/maps", mapObject.mapFolder)
    
    #make map directory
    try:
        os.makedirs(directory_path)
    except OSError as e:
        mapObject.delete()
        mapUserInstance.delete()
        return Response(status=500)
  
    #make marker directory
    directory_path = os.path.join(directory_path, "markers")
    
    try:
        os.makedirs(directory_path)
    except OSError as e:
        mapObject.delete()
        mapUserInstance.delete()
        return Response(status=500)
    
    #serializer map image:
    mapImage = imageSerializer(data=request.data)
    mapDestinationPath = os.path.join(settings.ROOT_FOLDER, "frontEnd/map-app/react-app/src/maps/", mapObject.mapFolder, "MAP_IMAGE.jpg")
    if mapImage.is_valid() is False:
        mapImagePath = os.path.join(settings.ROOT_FOLDER, "frontEnd/map-app/react-app/src/maps/", "MAP_IMAGE.jpg")
        shutil.copy(mapImagePath, mapDestinationPath)
        
    #check this
    else:
        mapImage = mapImage.validated_data['image']
        try:
            with open(mapDestinationPath, 'wb+') as new_image_file:
                new_image_file.write(mapImage.read())
        except Exception as e:
            return Response(status=500)
    return Response(status=201, data={'mapId': mapObject.id})
 
 
@api_view(['POST'])               
def addFriendToMap(request: Response) -> Response:
    #authenticate user and reciever
    user=userEquals(request)
    if user is None: return Response(status=408)
    tempVar = mapRequest(data=request.data)
    
    if tempVar.is_valid() is False:
        return Response(status=400)
    
    recId=tempVar.validated_data['recId']
    mapId=tempVar.validated_data['mapId']
    reqType=tempVar.validated_data['reqType']
    
    #ensure request is either collaborator or spectator
    if reqType not in [1,2]:
        Response(status=400)
        
        
    #authenticate user even has permissions to add (is a collaborator or owner)
    try:
        mapId = MAP.objects.get(id=mapId)
        checker = MAP_USER.objects.get(userId=user, mapId=mapId)
        #make sure spectator can just add more spectators
        if checker.status == 2 and reqType != 2:
            return Response(status=427)
    except ObjectDoesNotExist:
        return Response(status=427)

    #add them to the map by default instead of creating a mapRequest (since they are already Friends)
    #check if rec is even valid
    try:
        recId=USER.objects.get(name=recId)
        try:
            curr_relation = USER_RELATION.objects.get(user1=user,user2=recId)
            
            #if they are friends add a newMapUser
            if curr_relation.status==1:
                
                #ensure they arent already part of the map
                if MAP_USER.objects.filter(mapId=mapId, userId=recId, status=reqType).first() != None:
                    return Response(status=400)
                
                #valid request so proceed:
                new_instance=MAP_USER(mapId=mapId, userId=recId, status=reqType)
                new_instance.save()
                return Response(status=201)
            else:
                return Response(status=400)
            
        #edit the codes here
        except ObjectDoesNotExist:
            return Response(status=400)
        
    except ObjectDoesNotExist:
        return Response(status=400)
    
    
@api_view(['POST'])    
def getUserMaps(request: Response) -> Response:
    #authenticate suer
    user=userEquals(request)
    if user is None: return Response(status=408)
    #return list of current maps
    userMaps = MAP_USER.objects.filter(userId=user)
    list_of_mapId = [t.mapId.id for t in userMaps]
    return Response(status=201, data={'mapId': list_of_mapId})


def authTemplate(request: Response, func1: Callable) -> Callable:
    #authenticate user
    user=userEquals(request)
    if user is None: return Response(status=408)
    
    #authenticate mapId
    mapId=getMap(data=request.data)
    if mapId.is_valid() is False:
        return Response(status=400)
    mapId=mapId.validated_data['mapId']
    
    #authenticate this is a real map
    try:
        mapId=MAP.objects.get(id=mapId)
        #authenticate this map belongs to user
        try:
            #authenticate this map even has the user
            MAP_USER.objects.get(mapId=mapId, userId=user)
            
            #perform action    
            return func1(mapId,user,request)
    
        #edit the codes here  
        except ObjectDoesNotExist:
            return Response(status=400)
        
    except ObjectDoesNotExist:
        return Response(status=400)    


@api_view(['POST'])
def getMapFromId(request) -> Response:
    def discrete(mapId,user,request):
        mapData=mapSerializer(mapId)
        status = MAP_USER.objects.get(mapId=mapId, userId=user).status
        response_data = {
            'mapData': mapData.data,
            'status': status,
            'folderName': mapId.mapFolder,
        }
        return Response(status=201, data=response_data)
    return authTemplate(request=request, func1=discrete)


@api_view(['POST'])
def getMapUsers(request):
    def discrete(mapId,user,request):
        mapUsers=MAP_USER.objects.filter(mapId=mapId)
        mapUsers={i.userId.name: i.status for i in mapUsers}
        return Response(status=201,data=mapUsers)
    return authTemplate(request=request, func1=discrete)


#should only work for owner
@api_view(['POST'])
def editMapFeatures(request) -> Response:
    def discrete(mapId,user,request):
        pass
    return authTemplate(request=request, func1=discrete)


#delete map
@api_view(['POST'])
def deleteMap(request) -> Response:
    def discrete(mapId,user,request):
        curr_map_user = MAP_USER.objects.get(mapId=mapId, user=user)
        if curr_map_user.status == 0:
            mapId.delete()
            return
        else:
            curr_map_user.delete()
        return Response(status=201)
    return authTemplate(request=request, func1=discrete)


#ability for owner to remove a member or make them a spectator (fill in after implementing markers -- should destroy all user markers)
@api_view(['POST'])
def editPermission(request) -> Response:
    def discrete(mapId,user,request):
        pass
    return authTemplate(request=request, func1=discrete)


#do this at the end
@api_view(['POST'])
def getMapLink(request) -> Response:
    pass
