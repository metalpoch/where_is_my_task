from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Contact, Profile, Task


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'query_type', 'message']


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = Profile
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'gender',
            'work_area',
            'leader',
            'programming_area'
        )


class NewTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ('done', 'sender')
