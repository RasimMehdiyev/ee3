from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response



# Create your views here.
@api_view(['GET'])
def getLeaderboard(request):
    teams = Teams.objects.all()
    serializer = TeamsSerializer(teams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def updateLeaderboard(request, teamID, points):
    team = Teams.objects.get(id=teamID)
    team.points = points
    team.save()
    teams = Teams.objects.all()
    serializer = TeamsSerializer(teams, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getGameStats(request, id):
    game = Game.objects.get(id=id)
    serializer = GameSerializer(game, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getAllDummyData(request):
    dummy = DummyModel.objects.all()
    serializer = DummySerializer(dummy, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getDummyData(request, id):
    dummy = DummyModel.objects.get(id=id)
    serializer = DummySerializer(dummy, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createDummyData(request):
    data = request.data
    dummy = DummyModel.objects.create(
        randomNumber = data['randomNumber'],
        randomBoolean = data['randomBoolean'],
        randomString = data['randomString']
    )
    serializer = DummySerializer(dummy, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def checkKeyPadCode(request,id,keypadCode):
    if request.method == 'GET':
        # data = request.data
        code = ""
        # print(type(data['keypadCode']))
        if type(keypadCode) == list:
            # transform to string
            code = ''.join(keypadCode)
        else:
            code = keypadCode
        print(code)
        module = Modules.objects.get(id=id)
        if module.keypadCode == code:
            module.status = True
            module.save()
            return Response(1)
        else:
            return Response(0)
    