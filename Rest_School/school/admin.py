from django.contrib import admin
from .models import School, SClass, Student


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')


class SClassAdmin(admin.ModelAdmin):
    list_display = ('grade', 'school')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'sclass')


# Register your models here.
admin.site.register(School, SchoolAdmin)
admin.site.register(SClass, SClassAdmin)
admin.site.register(Student, StudentAdmin)

