from django.contrib import admin
from app.models import student
from app.models import courses
from app.models import courseregistration
# Register your models here.

admin.site.register(student)
admin.site.register(courses)
admin.site.register(courseregistration)