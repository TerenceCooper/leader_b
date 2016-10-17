from django.db import models
from django.conf import settings


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	team = models.CharField(default='', max_length=75)


	def __str__(self):
		return '{}'.format(self.team)



