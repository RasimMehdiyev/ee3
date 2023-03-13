from django.db import models


class Members(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Member'
        verbose_name_plural = 'Members'


class Teams(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    members = models.ManyToManyField('Members', blank=True, null=True)

    #team size for admin panel
    def team_size(self):
        return self.members.count()

    def __str__(self):
        return self.name

class Game(models.Model):
    team = models.ForeignKey('Teams', on_delete=models.CASCADE, blank=True, null=True)
    time_spent = models.IntegerField(blank=True, null=True)
    startedAt = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    timeBombModule = models.IntegerField(blank=True, null=True)
    timeLaserModule = models.IntegerField(blank=True, null=True)
    timePortalGunModule = models.IntegerField(blank=True, null=True)
    timeDrawBoxModule = models.IntegerField(blank=True, null=True)
    timeBlockBoxModule = models.IntegerField(blank=True, null=True)
    timeVoiceFilteringModule = models.IntegerField(blank=True, null=True)
    timePolarizedScreenModule = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['startedAt']
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

class Hints(models.Model):
    hint = models.TextField(blank = True , null = True)

    def __str__(self):
        return self.hint

class Modules(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False, blank=True, null=True)
    hint = models.ManyToManyField('Hints', blank=True, null=True)

    def __str__(self):
        return self.name

class DummyModel(models.Model):
    randomNumber = models.IntegerField(default = 0, blank=True, null=True)
    randomBoolean = models.BooleanField(default=False, blank=True, null=True)
    randomString = models.CharField(default="dummy", max_length=100, blank=True, null=True)

    def __str__(self):
        return self.randomString

