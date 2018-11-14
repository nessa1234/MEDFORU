"""med4u URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app1.views import HomepageView,ScheduleupListView,ScheduleDetailView,BookCreateView,BookAppointView
from app1.views import MainPage,MainPage1,DoctorView,DoclistView,ScheduleView,ScheduleListView,ScheduleUpdateView,DocListView,CancelView,FailureView,UserdetailView,SuccessView,UserlistView,UpdatedocView,DepartmentlistView,DetaildocView,AboutView,DepaddPage,RegisterCustomer,DepartmentView,DepartmentListView,HomeView,DepartDetailView,AdminPage
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.auth import views as auth_views
from app1 import views



urlpatterns = [
    url(r'^$',MainPage.as_view(),name='Main'),
    url(r'^main/',MainPage1.as_view(),name='Main1'),
    url(r'^userlist/',UserlistView.as_view(),name='Userlist'),
    url(r'^User/(?P<pk>[0-9]+)/$',UserdetailView.as_view(),name='User'),
    url(r'^Doc/',DoctorView.as_view(),name='Docdetail'),
    url(r'^DocList/',DoclistView.as_view(),name='Doclist'),
    url(r'^DocList2/',DocListView.as_view(),name='Doclist2'),
    url(r'^updated/(?P<pk>[0-9]+)/$',UpdatedocView.as_view(),name='update'),
    url(r'^docdetail/(?P<pk>[0-9]+)/$',DetaildocView.as_view(),name='Details'),
    url(r'^Register/',RegisterCustomer.as_view(),name='register'),
    url(r'^Departments/',DepartmentView.as_view(),name='Depart'),
    url(r'^DepartView/',DepartmentListView.as_view(),name='DepartView'),
    url(r'^DepartView2/',DepartmentlistView.as_view(),name='DepartView2'),

    url(r'^Depdtail/(?P<pk>[0-9]+)/$',DepartDetailView.as_view(),name='D_Detail'),
    url(r'^home/',HomeView.as_view(),name='D_View'),
    url(r'^home2/',HomepageView.as_view(),name='D_View2'),
    url(r'^adminpage/',AdminPage.as_view(),name='AdminPage'),
    url(r'^Departupdate/(?P<pk>[0-9]+)/$',DepaddPage.as_view(),name='Deprtadd'),
    url(r'^login/$',views.login, name='login'),
    url(r'^logout/$',auth_views.logout,name='logout'),
    url(r'^about/$',AboutView.as_view(),name='about'),
    # url(r'^calender/$',CalenderView.as_view(),name='calender')

    url(r'^BookCreate/',BookCreateView.as_view(),name='bookcreate'),
    url(r'^bookappoint/(?P<pk>[0-9]+)/$',BookAppointView.as_view(),name='bookappoint'),
    
    # url(r'^payment/$', views.payment, name="payment"),
    # url(r'^payment/success$', views.payment_success, name="payment_success"),
    # url(r'^payment/failure$', views.payment_failure, name="payment_failure"),

    url(r'^Schedule/$',ScheduleView.as_view(),name='Schedule'),
    url(r'^schedlst/',ScheduleListView.as_view(),name='schedule1'),
    url(r'^schdtl/(?P<pk>[0-9]+)/$',ScheduleDetailView.as_view(),name='scheduledet'),
    url(r'^Schedupdte/(?P<pk>[0-9]+)/$',ScheduleUpdateView.as_view(),name='schedule2'),
    url(r'^schedlst2/',ScheduleupListView.as_view(),name='schedule11'),

    



]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
