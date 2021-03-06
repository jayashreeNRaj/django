from django import forms
from home.models import Student
class StudentCreateForm(forms.Form):
    student_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Student Name'}))
    dept=(
        ('CSE','Computer Science'),
        ('MH','Mech'),
        ('CV','Civil')
    )
    department=forms.CharField(label='',widget=forms.Select(attrs={'class':'custom-select'},choices=dept))

class StudentEditModelForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        widgets={'student_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Student Name'}),
        'department':forms.Select(attrs={'class':'custom-select'})
        }
class StudentSearchForm(forms.Form):
    q=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','placeholder':'Search'}))