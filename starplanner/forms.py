from django import forms
from django.forms import ModelForm
from .models import Task, Comment


class TaskForm(ModelForm):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, widget=forms.RadioSelect(attrs={'class':'form-control'}))

    class Meta:
        model = Task
        fields = '__all__'
        labels = {
            'task': 'Task',
            'user': 'User',
            'priority': 'Priority',
            'description': 'Description',
        }
        widgets = {
            'task':forms.NumberInput(attrs={'placeholder':'e.g 1', 'class':'form-control'}),
            'user':forms.TextInput(attrs={'placeholder':'e.g Jbloggs', 'class':'form-control'}),
            'description':forms.Textarea(attrs={'placeholder':'Describe Your Task Here', 'class':'form-control'}),
        }


    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 10:
            raise forms.ValidationError("Description must be at least 10 characters long")
        return description
    

    def clean_user(self):
        user = self.cleaned_data['user']
        if len(user) < 2:
            raise forms.ValidationError("Username must be at least 2 characters long")
        return user
    

    def clean(self):
        cleaned_data = super().clean()
        priority = cleaned_data.get('priority')
        description = cleaned_data.get('description')

        if priority == 'high' and (not description or len(description) < 20):
            raise forms.ValidationError("High priority tasks must have a detailed description (at least 20 characters)")

        return cleaned_data


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('task', 'author', 'body')
        labels = {
            'task': 'Task',
            'author': 'Author',
            'body': 'Comment content',
        }
        widgets = {
            'task':forms.NumberInput(attrs={'placeholder':'e.g 1', 'class':'form-control'}),
            'author':forms.TextInput(attrs={'placeholder':'e.g Jbloggs', 'class':'form-control'}),
            'body':forms.Textarea(attrs={'placeholder':'write your comment here', 'class':'form-control'}),
        }
    def clean_task(self):
        task_id = self.cleaned_data['task']
        try:
            task = Task.objects.get(pk=task_id)
            return task
        except Task.DoesNotExist:
            raise forms.ValidationError("Task does not exist")
        

    def clean_author(self):
        author = self.cleaned_data['author']
        if len(author) < 2:
            raise forms.ValidationError("Author name must be at least 2 characters long")
        return author
    

    def clean_body(self):
        body = self.cleaned_data['body']
        if len(body) < 10:
            raise forms.ValidationError("Comment must be at least 10 characters long")
        return body