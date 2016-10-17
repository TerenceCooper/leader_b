from django.db import models
from django.conf import settings


class Document(models.Model):
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	created = models.DateTimeField(auto_now_add=True)
	rmse = models.DecimalField(max_digits=16, decimal_places=6, default=99)

	class Meta:
		ordering = ('rmse', '-created')
