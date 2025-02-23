from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset
from .models import Task, Comment


class TaskForm(ModelForm):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]

    priority = forms.ChoiceField(
        choices=PRIORITY_CHOICES,
        widget=forms.RadioSelect()
    )

    class Meta:
        model = Task
        fields = ['title', 'priority', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe Your Task Here',
                'class': 'form-control'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                "Task Information",
                Field('title'),
                Field('description'),
            ),
            Fieldset(
                "Task Priority",
                Field('priority'),
            ),
            Submit('submit', 'Save Task', css_class="btn btn-primary")
        )

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 10:
            raise forms.ValidationError(
                "Description must be at least 10 characters long"
            )
        return description

    def clean(self):
        cleaned_data = super().clean()
        priority = cleaned_data.get('priority')
        description = cleaned_data.get('description')

        if priority == 'high' and (not description or len(description) < 50):
            raise forms.ValidationError(
                "High priority tasks must have a detailed description "
                "(at least 50 characters)"
            )
        return cleaned_data


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('body'),
        )
        self.helper.add_input(Submit('submit', 'Add Comment'))
