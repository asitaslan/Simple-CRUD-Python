import uuid
from django.db import models
from django.utils.http import int_to_base36


ID_LENGTH = 36
first_length = 8
second_lenght = 4
third_lenght = 4
forth_lenght = 4
last_legth = 12

def id_gen() -> str:
    first = int_to_base36(uuid.uuid4().int)[:first_length]
    second = int_to_base36(uuid.uuid4().int)[:second_lenght]
    third = int_to_base36(uuid.uuid4().int)[:third_lenght]
    forth = int_to_base36(uuid.uuid4().int)[:forth_lenght]
    last = int_to_base36(uuid.uuid4().int)[:last_legth]
    return f'{first}-{second}-{third}-{forth}-{last}'


# Create your models here.
class Practice(models.Model):
    id = models.CharField(max_length=ID_LENGTH, primary_key=True, default=id_gen, editable=False)
    title = models.CharField(max_length=250)
    problem = models.CharField(max_length=400)
    point = models.IntegerField()
    level = models.CharField(max_length=25)
    language = models.CharField(max_length=15)
    input = models.CharField(max_length=100,blank=True)
    expected_output = models.CharField(max_length=200)

    def __str__(self):
        return self.title
