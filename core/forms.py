from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from .models import Address, User, Contact, Department, Education, Doctor, Patient, Hospital, DaySchedule, Appointment


class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'validate'
            })


class PatientSignupForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
