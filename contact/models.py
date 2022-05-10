from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


def validate_name(value):
    if type(value)==str and len(value)>=5 :
        return value
    else:
        raise ValidationError("Invalid name")


class Contact(models.Model):
    name = models.CharField(max_length=30,validators=[validate_name])
    phone_num = models.BigIntegerField(unique=True)
    address = models.CharField(max_length=255, default='Y')

    class Meta:
        db_table = 'EMPLOYEE_MASTER'
        ordering = ['name']


class Group(models.Model):
     name = models.CharField(max_length=30)
     contref = models.ForeignKey(Contact, on_delete=models.CASCADE)

     class Meta:
        db_table = 'Group_db'
        ordering = ['name']