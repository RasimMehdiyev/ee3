from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response



# Create your views here.
@api_view(['GET'])
def getLeaderboard(request):
    # filter based on points
    teams = Teams.objects.all()
    serializer = TeamsSerializer(teams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def updateLeaderboard(request, teamID, points):
    team = Teams.objects.get(id=teamID)
    team.points = team.points + points
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
    
@api_view(['GET'])
def startTimer(request):
    timer = TimerModule.objects.get(id=1)
    if timer.startTimer == True:
        return Response(1)
    else:
        return Response(0)
    
@api_view(['GET'])
def setModuleStatus(request, id , status):
    if request.method == 'GET':
        module = Modules.objects.get(id=id)
        if status == 1:
            module.status = True
        else:
            module.status = False
        module.save()
        moduleName = module.name
        return Response({'status': module.status,'message': '{}\'s status updated successfully to '.format(moduleName) + str(module.status) + ''})
    
@api_view(['GET', 'POST'])
def teams(request):
    if request.method == 'GET':
        teams = Teams.objects.all()
        serializer = TeamsSerializer(teams, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # first create members model using MembersSerializer
        serializer = MembersSerializer(data=request.data['members'], many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # take members id's from serializer.data
        members_local = []
        for member in serializer.data:
            members_local.append(member['id'])
        print(members_local)

        data = request.data
        team = Teams.objects.create(
            name = data['name'],
            points = data['points'],
            # add members id's to team
        )
        team.members.add(*members_local)
        serializer = TeamsSerializer(team, many=False)
        return Response(serializer.data)