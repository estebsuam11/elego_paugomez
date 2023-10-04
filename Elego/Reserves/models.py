from django.db import models

    
# crear los modelos aqui

class Reserve(models.Model):
    
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=15)
    zip_code = models.IntegerField()
    service = models.CharField(max_length=30)
    date =  models.DateField()
    number_hour = models.IntegerField()
    start_time = models.DateTimeField()
    pets = models.CharField(max_length= 10)
    pet_number = models.IntegerField()