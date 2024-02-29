from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Words
from .serializers import WordSerializer

@api_view(['GET'])
def getData(request):
    wordItems = Words.objects.all()
    serializer = WordSerializer(wordItems, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addWord(request):
    serializer = WordSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)