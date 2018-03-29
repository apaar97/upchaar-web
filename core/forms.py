from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from .models import Address, User, Contact, Department, Education, Doctor, Patient, Hospital, DaySchedule, Appointment


class UserSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'validate'
            })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email, role=self.instance.role).exclude(username=username).exists():
            raise forms.ValidationError(u'A user with that email address already exists.')
        return email


class PatientSignupForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('patient_desc',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'validate'
            })
