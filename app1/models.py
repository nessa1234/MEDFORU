from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import calendar


INACTIVE = 0
ACTIVE = 1
STATUS = ((INACTIVE, 'Inactive'),(ACTIVE, 'Active'))



DEPART_CHOICES=(
	('GYNECOLOGY','Gynecology'),
	('PEDIATRICS','Pediatrics'),
	('CARDIOLOGY','Cardiology'),
	('ORTHOPAEDICS','Orthopaedics'),
				)

class Customer(models.Model):
     user_data = models.OneToOneField(User)
     place = models.CharField(max_length=50)
     address = models.CharField(max_length=50)
     zipcode = models.IntegerField()


     def __str__(self):
          return "%s %s" % (self.user_data.first_name, self.user_data.last_name)

class Booking(models.Model):
    booking_id=models.ForeignKey(Customer)
    def __str__(self):
        return self.booking_id
                        

# Create your models here.
class Department(models.Model):
    depart_name=models.CharField(max_length=50)
    depart_photo=models.ImageField(upload_to='media/staff_img/Department')
    depart_description=models.CharField(max_length=1000)
    create_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.depart_name

class Doctors(models.Model):
    Doc_name=models.CharField(max_length=50)
    Doc_Speciality=models.ForeignKey(Department,default=None)
    Doc_age=models.IntegerField(default=18)
    Doc_email=models.EmailField()
    Doc_photo=models.ImageField(upload_to='media/staff_img/doctors')
    create_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Doc_name

# ****************Department****************************
# class Department(models.Model):
#     name = models.CharField(max_length=50)
#     director = models.ForeignKey(User, null=True)
#     staff = models.ManyToManyField(User, related_name='+')

#     def __unicode__(self):
# return self.name

#***************************REGISTER***********************



class Schedule(models.Model):
    dc_name=models.ForeignKey(Doctors,default=None)
    day = models.DateField(default=None)
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
    num_ppl=models.IntegerField(default=None)
    create_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.dc_name

class Bookmodel(models.Model):
    user_name=models.CharField(max_length=20)
    doctor_name=models.CharField(max_length=20)
    date_appointment=models.DateField(blank=True)
    s_time=models.TimeField(blank=True)
    e_time=models.TimeField(default=None,blank=True)
    fees=models.IntegerField(default=300)
    no_ppl=models.IntegerField(default=1)
    create_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user_name


