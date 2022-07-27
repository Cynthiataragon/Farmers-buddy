from django.db import models

# Create your models here.
#climate and soil 

class Dataset(models.Model):
	location = models.CharField(max_length= 200)
	soil = models.CharField(max_length= 200)
	weather = models.CharField(max_length= 200)
	crop = models.CharField(max_length= 200)

	
	#making the database readable
	def __str__(self):
		return self.location
