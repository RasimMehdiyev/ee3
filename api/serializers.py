from rest_framework import serializers
from .models import *


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class DummySerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyModel
        fields = '__all__'