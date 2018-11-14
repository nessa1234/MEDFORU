# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app1.models import Doctors,Customer,Department,Schedule,Bookmodel


# Register your models here.
admin.site.register(Doctors)
admin.site.register(Customer)
admin.site.register(Department)
admin.site.register(Schedule)
admin.site.register(Bookmodel)