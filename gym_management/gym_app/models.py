from django.db import models

# Create your models here.
class customers(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200,primary_key=True)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200,null=True)
    fee = models.IntegerField(null=True)
    fee_status = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.name

class trainer(models.Model):
    customers = models.ForeignKey(customers, null=True, on_delete= models.SET_NULL)
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200,primary_key=True)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200,null=True)
    salary = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return self.name