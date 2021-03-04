from rest_framework import serializers
from rest_framework.response import Response
from App.models import MusicModel,ShowDataModel

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicModel
        fields = '__all__'   
class ShowDataSerializer(serializers.ModelSerializer):
    show = serializers.SerializerMethodField()
    class Meta:
        model = ShowDataModel
        fields = '__all__'
    def get_show(self,obj):
        #print(obj)
        #import pdb; pdb.set_trace()
        #print(obj.id)
        # aaa= MusicSerializer(MusicModel.objects.filter(title=obj.select),many=True).data
        # print(aaa)
        # print(aaa[0]['song'])
        #if you want a queryset data so use this print(aaa[0]['song'])
        # import pdb; 
        # pdb.set_trace()
        # print("run")
        data = MusicModel.objects.get(title=obj.select)
        context = {
            "ID":data.id,
            "Title":data.title,
            "Contributors": data.contributors,
            "ISWC": data.iswc,
            "Source":data.source,
            "Song":'http://localhost:8000'+data.song.url
        }
        return (context)