from django.db import models
from datetime import *

current_date = datetime.date.today()

class FamilyMember(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField()
    phone_number = models.IntegerField()

    def age(self):
        return current_date.year - self.birthdate.year

    def full_name(self):
        return f'{self.name} {self.surname}'