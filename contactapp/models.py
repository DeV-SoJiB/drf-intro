from django.db import models


# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self) -> str :
        return self.name
    

class Authors(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str :
        return self.name
    

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)

    def __str__(self) -> str :
        return self.title