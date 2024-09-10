from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    # define enum for limited choices
    CHAI_TYPE_CHOICE = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELACHI')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')

    # to modify the display of object(records) added in the model
    def __str__(self):
        return self.name
    
# one to many relationship
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    # foreign key arguments - model name
    # ON DELETE CASCADE is used to specify that when a row is deleted from the parent table, all rows in the child table that reference the deleted row should also be deleted.
    # This is useful for maintaining the integrity of the database.
    # related name represents the name of the current table that needs to be inserted in the other table for which we are establishing the relationship 
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return f'{self.user.userName} review for {self.chai.name}'
    

# many to many relationship
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ChaiVarieties = models.ManyToManyField(ChaiVariety, related_name="stores")

    def __str__(self) :
        return self.name
    
# one to one relationship
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety,on_delete=models.CASCADE, related_name="certificate")
    number = models.CharField(max_length=100)
    issuedDate = models.DateTimeField(default=timezone.now)
    validUntil = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'