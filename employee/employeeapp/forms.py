from django import forms
from.models import Employee


class EmployeeForm(forms.ModelForm):

     # meta class is a inner class for django models its used to change the behaviour of models.
    class Meta:
        model=Employee
        fields='__all__'


    def __init__(self,*args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label="pleace choose your position"

        
        

       