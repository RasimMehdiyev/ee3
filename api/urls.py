from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('leaderboard/', getLeaderboard, name='leaderboard'),
    path('leaderboard/<int:teamID>/<int:points>/', updateLeaderboard, name='leaderboard'),
    path('get_dummy/', getAllDummyData, name='get_dummy'),
    path('get_dummy/<str:id>/', getDummyData, name='get_dummy'),
    path('create_dummy/', createDummyData, name='create_dummy'),
    path('send_code/<int:id>/<str:keypadCode>/', checkKeyPadCode, name='send_code'),
    path('start-timer/' , startTimer , name='start-timer'),
    path('set-status/<int:id>/<int:status>/', setModuleStatus, name='set-status'),
]