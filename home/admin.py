from django.contrib import admin
from home.models import Student,library,Section,book,Teacher
#from .model import Student
# Register your models here.
#admin.site.register(Student)
#admin.site.register(library)
"""admin.site.register(Section)
admin.site.register(book)
admin.site.register(Teacher)"""
@admin.register(book)
class bookAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # pass
    search_fields=('student_name',"usn",'department')
    list_filter=('student_name',"usn",'timestamp','department')
    fields=('student_name',"usn",'department')

@admin.register(library)
class libraryAdmin(admin.ModelAdmin):
    pass

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


