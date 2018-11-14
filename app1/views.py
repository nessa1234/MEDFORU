# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,ListView,UpdateView,DetailView,FormView
from app1.forms import DoctorForm,UserForm,CustomerForm,DepartForm,BookForm,ScheduleForm
from app1.models import Doctors,Customer,Department,Schedule,Bookmodel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test
    
@login_required
def home(request):
    return render(request, 'core/home.html')


class HomeView(ListView):
    template_name='home.html'
    model=Doctors
    context_object_name='D_lst_home'



# Create your views here.
#***************************MAIN PAGE*****************************************
class MainPage(TemplateView):
	template_name='medi.html'
class MainPage1(TemplateView):
    template_name='medi.html'


#**************************DOCTOR******************************
class DoctorView(CreateView):
	template_name='Docdetail.html'
	form_class=DoctorForm
	success_url='success'
class DoclistView(ListView):
	template_name="doclist.html"
	model=Doctors
	context_object_name="DoclistView" 
class DocListView(ListView):
    template_name="doclist2.html"
    model=Doctors
    context_object_name="DocListView" 

class UpdatedocView(UpdateView):
    form_class= DoctorForm
    template_name="Updated.html"
    model=Doctors
    context_object_name='update'
    success_url='/DocList/'
class DetaildocView(DetailView):
	template_name="details.html"
	model=Doctors
	context_object_name='details'
# *****************************************REGISTER************************************************




class RegisterCustomer(FormView):
     template_name = 'register.html'
     form_class = UserForm
     model = User

     def get(self,request,*args,**kwargs):
         self.object = None
         form_class = self.get_form_class()
         user_form = self.get_form(form_class)
         cust_form = CustomerForm()
         return self.render_to_response(self.get_context_data(form1=user_form,form2=cust_form))

     def post(self,request,*args,**kwargs):
         self.object = None
         form_class = self.get_form_class()
         user_form = self.get_form(form_class)
         cust_form = CustomerForm(self.request.POST, self.request.FILES)
         if (user_form.is_valid() and cust_form.is_valid()):
             return self.form_valid(user_form, cust_form)
         else:
             return self.form_invalid(user_form, cust_form)

     def get_success_url(self, **kwargs):
         return ('success')

     def form_valid(self, user_form, cust_form):
         self.object = user_form.save()
         self.object.is_staff=True
         self.object.save()
         cust_obj = cust_form.save(commit=False)
         cust_obj.user_data = self.object
         cust_obj.save()
         return redirect('/login/')

     def form_invalid(self, user_form, cust_form):
         return self.render_to_response(self.get_context_data(form1=user_form,form2=cust_form))
		
# ***************************************Departments************************************************
class DepartmentView(CreateView):
    template_name='department.html'
    form_class=DepartForm
    success_url='success'
class DepartmentListView(ListView):
    template_name="deprtList.html"
    model= Department
    context_object_name='DepartmentListView' 
# class DepartDetailView(DetailView):
#     template_name="D_detail.html"
#     model=Department
#     context_object_name='D_detail'
class DepaddPage(UpdateView):
    form_class= DepartForm
    template_name="UpdateDep.html"
    model=Department
    context_object_name='updatedep'
    success_url='/deprtList/'
class DepartmentlistView(ListView):
    template_name="deprtList2.html"
    model= Department
    context_object_name='DepartlistView' 
#*******************************************DOCTORS*****************************************

# ****************************************BOOKING***************************************************

class AdminPage(TemplateView):
    template_name='adminhome.html'
class SuccessView(TemplateView):
    template_name='success.html'
class CancelView(TemplateView):
    template_name='cancel.html'
class FailureView(TemplateView):
    template_name='failure.html'
class BookCreateView(CreateView):
    template_name='book.html'
    form_class=BookForm
    success_url='success'



#*******************************USER****************************
class UserlistView(ListView):
    template_name="user.html"
    model= Customer
    context_object_name='UserlistView' 

class UserdetailView(DetailView):
    template_name="userdetail.html"

    model=Customer
    success_url='success'
    context_object_name='Userdetail'

class HomepageView(TemplateView):
    template_name='homepage.html'


def login(request):
     form =AuthenticationForm()
     if request.user.is_authenticated():
         if request.user.is_superuser:
             return redirect("/adminpage/")# or your url name
         if request.user.is_staff:
             return redirect("/D_View/")# or your url name


     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = auth.authenticate(username=username, password=password)

         if user is not None:
             # correct username and password login the user
             auth.login(request, user)
             if request.user.is_superuser:
                 return redirect("/adminpage/")# or your url name
             if request.user.is_staff:
                 return redirect("/home2/")# or your url name

         else:
             messages.error(request, 'Error wrong username/password')
     context = {}
     context['form']=form

     return render(request, 'Login.html', context)

@user_passes_test(lambda u: u.is_staff)
def StaffHome(request):
     context = {}
     return render(request, 'homepage.html', context)

@user_passes_test(lambda u: u.is_superuser)
def AdminHome(request):
     context = {}
     return render(request, 'adminhome.html', context)
    

class AboutView(TemplateView):
    template_name='about.html'

# *****************************calender**************************






#******************************Schedule***********************



class ScheduleView(CreateView):
    template_name='Schedule.html'
    form_class= ScheduleForm
    success_url='success'
   
class ScheduleListView(ListView):
    template_name='schedule1.html'
    model=Schedule
    context_object_name='Schedule'

class ScheduleupListView(ListView):
    template_name='schedule11.html'
    model=Schedule
    context_object_name='Schedule1'

class ScheduleDetailView(DetailView):
    template_name='scheddetail.html'
    model=Schedule
    context_object_name='scheddetail'
    success_url='success'

class ScheduleUpdateView(UpdateView):
    form_class= ScheduleForm
    template_name="UpSchedule.html"
    model= Schedule
    context_object_name='SchedUp'
    success_url='/Schedule/'


class DepartDetailView(DetailView):
    template_name='D_detail.html'
    def get(self,request,pk):
        d_id=pk
        d_detail= Department.objects.get(id=d_id)
        doc_detail= Doctors.objects.filter(Doc_Speciality=d_id)
        context={
            'd_detail':d_detail,
            'doc_detail':doc_detail,
                }
        return render(request,self.template_name,context)

# class ScheduleDetailView(DetailView):
#     template_name='scheddetail.html'
#     def get(self,request,pk):
#         s_id=pk
#         doct_detail= Doctors.objects.get(id=s_id)
#         sch_detail= Schedule.objects.filter(dc_name=s_id)
#         context={
#         'doct_detail':doct_detail,
#         'sch_detail':sch_detail,s
#         }
#         return render(request,self.template_name,context)



class BookAppointView(DetailView):
    template_name='appoint.html'
    context_object_name='appoint'



    def get(self,request,pk):
        a_id=pk
        sched_detail=Schedule.objects.get(id=a_id)
        docname=sched_detail.dc_name
        day=sched_detail.day
        s_time=sched_detail.start_time
        e_time=sched_detail.end_time
        no_ppl=sched_detail.num_ppl
        context={
        'docname':docname,
        'day':day,
        's_time':s_time,
        'e_time':e_time,
        'no_ppl':no_ppl,
        }
        return render(request,self.template_name,context)

    def post(self,request,pk):
        a_id=pk
        sched_detail=Schedule.objects.get(id=a_id)
        docname=sched_detail.dc_name
        day=sched_detail.day
        s_time=sched_detail.s_time
        e_time=sched_detail.e_time
        no_ppl=sched_detail.num_ppl
        context={
        'docname':docname,
        'day':day,
        's_time':s_time,
        'e_time':e_time,
        'no_ppl':no_ppl,
        }
        

        Bookmodel.objects.Create(
            user_name=request.user.username,
            docname=docname,
            day=day,
            s_time=s_time,
            e_time=e_name,
            no_ppl=no_ppl
        )
        
        return render(request,self.template_name,context)

        

    
#***********************


