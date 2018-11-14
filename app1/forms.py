from django import forms
from app1.models import Doctors,Department,Bookmodel,Schedule


from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from app1.models import Customer





class UserForm(UserCreationForm):
     class Meta:
         model = User
         fields = ['username','first_name','last_name','email','password1','password2']

class CustomerForm(forms.ModelForm):
     class Meta:
         model = Customer
         exclude = ('create_date','user_data')

class DoctorForm(forms.ModelForm):
    class Meta():
        model=Doctors
        exclude=("create_date",)


class DepartForm(forms.ModelForm):
    class Meta():
        model=Department
        exclude=('create_date',)

class BookForm(forms.ModelForm):
	class Meta():
		model=Bookmodel
		exclude=("create_date",)

class ScheduleForm(forms.ModelForm):
	class Meta():
		model=Schedule
		exclude=("create_date",)

		
		
