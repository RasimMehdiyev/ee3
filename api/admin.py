from django.contrib import admin

# Register your models here.

from .models import *

class TeamsAdmin(admin.ModelAdmin):
    list_display = ('name', 'points', 'team_size')
admin.site.register(Teams, TeamsAdmin)

class MembersAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Members, MembersAdmin)

class GameAdmin(admin.ModelAdmin):
    list_display = ('team', 'time_spent', 'startedAt', 'timeBombModule', 'timeLaserModule', 'timePortalGunModule', 'timeDrawBoxModule', 'timeBlockBoxModule', 'timeVoiceFilteringModule', 'timePolarizedScreenModule')
admin.site.register(Game, GameAdmin)

class HintsAdmin(admin.ModelAdmin):
    list_display = ('hint',)
admin.site.register(Hints, HintsAdmin)

class ModulesAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'status','keypadCode',)
admin.site.register(Modules, ModulesAdmin)

class DummyAdmin(admin.ModelAdmin):
    list_display = ('randomString','randomNumber','randomBoolean')
admin.site.register(DummyModel, DummyAdmin)

class TimerModuleAdmin(admin.ModelAdmin):
    list_display = ('id','startTimer')
admin.site.register(TimerModule, TimerModuleAdmin)

