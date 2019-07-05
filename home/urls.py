from django.urls import path
from django.contrib import admin
from .views import *
urlpatterns = [
    path('',home_view,name='home'),
    #path('',views,.home_view)
    path('delete-student/<id>',deletestudent),
    path('edit-student/<id>',editstudent),
    path('create-student/',createstudent),
    path('admin/', admin.site.urls),
]
