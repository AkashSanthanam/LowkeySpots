from django.urls import path
from .views import makeMap, addFriendToMap, getMapUsers, getUserMaps, getMapFromId, editMapFeatures

urlpatterns = [
    path('make-map/', makeMap),
    path('add-friend/', addFriendToMap),
    path('get-users/', getMapUsers),
    path('getUserMaps/', getUserMaps),
    path('get-map/', getMapFromId),
    path('edit/', editMapFeatures),
]