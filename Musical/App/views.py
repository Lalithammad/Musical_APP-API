from django.shortcuts import render
from App.models import MusicModel,ShowDataModel
from App.serializers import MusicSerializer,ShowDataSerializer
from rest_framework import viewsets
# Create your views here.
class MusicAPI(viewsets.ModelViewSet):
    queryset = MusicModel.objects.all()
    serializer_class = MusicSerializer
class ShowDataAPI(viewsets.ModelViewSet):
    queryset = ShowDataModel.objects.all()
    serializer_class = ShowDataSerializer    