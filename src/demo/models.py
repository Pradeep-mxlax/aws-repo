from enum import unique
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length =50 )
    

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length =50 )

    
    def __str__(self):
        return self.name 
    
class State(models.Model):
    name = models.CharField(max_length =50 )
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    district = models.ManyToManyField(District) 
    
    def __str__(self):
        return self.name





from datetime import date


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline



# from xmlrpc.client import DateTime
# new role: QualiltyAnalyst and qamanager in user table
# class AssigmentData(models.Model):
#     recurrence_period= (
#         	('Weekly','Weekly'),
# 			('Monthly','Monthly')  )
	
#     name = models.CharField(max_length = 100)
#     reviewer= models.ForeignKey(user, on_delete=models.CASCADE, related_name='reviewer')
#     blind_review = models.BooleanField(default=False)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     recurrence = models.CharField(max_length=15,choices=recurrence_period)
#     channels = models.JSONField( null=True )
#     filters = models.JSONField( null=True )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Assignment(models.Model):
#     assign_status=(
# 		('Pending','Pending'),
# 	 	('Complete','Complete')
#     )

#     refkey = models.CharField(max_length=50,default=_createHash)
#     AssigmentData = models.ForeignKey(AssigmentData, on_delete=models.CASCADE, related_name='assign_data')
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     status =  models.CharField(max_length=15,choices=Complete)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class assingment_reviewee(models.Model):
# 	assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='assingment')
# 	reviewee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewee')

#     class Meta: 
#         unique_together = ('assignment','reviewee')

# class TicketAssignment(models.Model):
# 	assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE(), related_name='assignment')
# 	ticket = models.ManyToManyField(Ticket)
# 	status = models.CharField(max_length=15, choices=eval_status)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)
 






#  from django.db import models
# from users.models import User
# from tickets.models import Ticket
# # Create your models here.


# class AssigmentData(models.Model):
#     recurrence_period= (
#         	('Weekly','Weekly'),
# 			('Monthly','Monthly')  )
	
#     name = models.CharField(max_length = 100)
#     reviewer= models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer')
#     blind_review = models.BooleanField(default=False)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     recurrence = models.CharField(max_length=15,choices=recurrence_period)
#     channels = models.JSONField( null=True )
#     filters = models.JSONField( null=True )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Assignment(models.Model):
#     assign_status=(
# 		('Pending','Pending'),
# 	 	('Complete','Complete')
#     )

#     refkey = models.CharField(max_length=50, default=_createHash)
#     AssigmentData = models.ForeignKey(AssigmentData, on_delete=models.CASCADE, related_name='assign_data')
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     status =  models.CharField(max_length=15, choices=Complete)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class assingment_reviewee(models.Model):
# 	assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='assingment')
# 	reviewee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewee')

#     class Meta: 
#         unique_together = ('assignment','reviewee')

# class TicketAssignment(models.Model):
# 	assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE(), related_name='assignment')
# 	ticket = models.ManyToManyField(Ticket)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)





