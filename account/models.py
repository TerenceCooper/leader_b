from django.db import models
from django.contrib.auth.models import User


# make user email field unique
User._meta.get_field('email')._unique = True


class Profile(models.Model):
	user = models.OneToOneField(User)
	team = models.CharField(max_length=75)


	def __str__(self):
		return '{}'.format(self.team)



