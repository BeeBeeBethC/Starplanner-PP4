from django import forms
from .models import Task, Profile

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields= '__all__'
        labels = {
            'task': 'Task',
            'user': 'User',
            'priority': 'Priority',
            'description': 'Description',
        }
        widgets = {
            'task':forms.NumberInput(attrs={'placeholder':'e.g 1', 'class':'form-control'}),
            'user':forms.TextInput(attrs={'placeholder':'e.g Jbloggs', 'class':'form-control'}),
            'priority':forms.RadioSelect(attrs={'choices': 'PRIORITY_CHOICES', 'class':'form-control'}),
            'description':forms.Textarea(attrs={'placeholder':'Describe Your Task Here', 'class':'form-control'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'phone']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)