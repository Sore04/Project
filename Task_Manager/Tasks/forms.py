from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']  # Exclude 'status'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'description': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full px-4 py-2 border rounded-lg'}),
        }
