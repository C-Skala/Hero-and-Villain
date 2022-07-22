from django.db import models

# Create your models here.

class Supers(models.Model):
    name = models.CharField(max_length= 200)
    alter_ego = models.CharField(max_length=200)
    Primary_ability = models.CharField(max_length= 200)
    secondary_ability = models.CharField(max_length= 200)
    catchphrase = models.CharField(max_length= 200)
    super_type = forign key