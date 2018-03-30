from django.conf import settings
from django.contrib.auth import login, authenticate
from django.core import serializers as django_serializers
from django.shortcuts import render, redirect, reverse
from django import forms
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from .models import User, Contact, Department, Doctor, Patient, Hospital, DaySchedule, Appointment
from .serializers import *
from .forms import UserSignUpForm, DoctorSignupForm, HospitalSignupForm


@api_view(['POST'])
def api_login(request, user=None):
    if not user:
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Login Failed'}, status=HTTP_401_UNAUTHORIZED)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'role': user.role,
        'token': token.key})


@api_view(['POST'])
def api_logout(request):
    id = request.data.get('id')
    if not id:
        return Response({'error': 'Invalid Request'}, status=HTTP_401_UNAUTHORIZED)

    try:
        user = User.objects.get(id=id)
        auth_token = user.auth_token
    except:
        return Response({'error': 'Invalid Request'}, status=HTTP_401_UNAUTHORIZED)

    user.auth_token.delete()
    return Response({'id': id, 'token': auth_token.key}, status=HTTP_200_OK)


@api_view(['POST'])
def get_auth_token(request):
    id = request.data.get('id')
    if not id:
        return Response({'error': 'Invalid Request'}, status=HTTP_401_UNAUTHORIZED)

    try:
        user = User.objects.get(id=id)
        auth_token = user.auth_token
    except:
        return Response({'error': 'Invalid Request'}, status=HTTP_401_UNAUTHORIZED)

    return Response({'id': id, 'token': auth_token.key}, status=HTTP_200_OK)


def signup(request):
    return render(request=request, template_name='signup/signup.html')


def signup_patient(request):
    if request.method == 'POST':
        userform = UserSignUpForm(request.POST, prefix='userform')
        # patientform = PatientSignupForm(request.POST, prefix='patientform')
        if userform.is_valid():
            user = userform.save()
            user.role = User.PATIENT
            user.date_of_birth = request.POST.get('date_of_birth')
            user.save()
            patient = Patient(user=user)
            patient.save()
            username = userform.cleaned_data.get('username')
            raw_password = userform.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        userform = UserSignUpForm(prefix='userform')
        # patientform = PatientSignupForm(request.POST, prefix='patientform')
    return render(request=request, template_name='signup/signup_patient.html',
                  context={'userform': userform})


def signup_doctor(request):
    if request.method == 'POST':
        userform = UserSignUpForm(request.POST, prefix='userform')
        doctorform = DoctorSignupForm(request.POST, prefix='doctorform')
        if userform.is_valid() and doctorform.is_valid():
            user = userform.save()
            user.role = User.DOCTOR
            user.date_of_birth = request.POST.get('date_of_birth')
            user.save()
            doctor = doctorform.save()
            doctor.user = user
            doctor.save()
            username = userform.cleaned_data.get('username')
            raw_password = userform.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        userform = UserSignUpForm(prefix='userform')
        doctorform = DoctorSignupForm(request.POST, prefix='doctorform')
    return render(request=request, template_name='signup/signup_doctor.html',
                  context={'userform': userform, 'doctorform': doctorform})


def signup_hospital(request):
    if request.method == 'POST':
        userform = UserSignUpForm(request.POST, prefix='userform')
        userform.fields['first_name'].widget = forms.HiddenInput()
        userform.fields['last_name'].widget = forms.HiddenInput()
        hospitalform = HospitalSignupForm(request.POST, prefix='hospitalform')
        if userform.is_valid() and hospitalform.is_valid():
            user = userform.save()
            user.role = User.HOSPITAL
            user.save()
            hospital = hospitalform.save()
            hospital.user = user
            hospital.save()
            username = userform.cleaned_data.get('username')
            raw_password = userform.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        userform = UserSignUpForm(prefix='userform')
        userform.fields['first_name'].widget = forms.HiddenInput()
        userform.fields['last_name'].widget = forms.HiddenInput()
        hospitalform = HospitalSignupForm(request.POST, prefix='hospitalform')
    return render(request=request, template_name='signup/signup_hospital.html',
                  context={'userform': userform, 'hospitalform': hospitalform})


def dashboard(request):
    if request.user.role == User.PATIENT:
        return render(request=request, template_name='dashboard/dashboard_patient.html')
    elif request.user.role == User.DOCTOR:
        return render(request=request, template_name='dashboard/dashboard_doctor.html')
    else:
        return render(request=request, template_name='dashboard/dashboard_hospital.html')


def dashboard_doctor(request):
    return render(request=request, template_name='dashboard/dashboard_doctor.html')


def dashboard_hospital(request):
    return render(request=request, template_name='dashboard/dashboard_hospital.html')


def book_appointment(request):
    return render(request=request, template_name='book_appointment_map.html')


def filter_appointment(request):
    return render(request=request, template_name='filter_appointment.html')


def calendar_appointment(request):
    dayschedules = django_serializers.serialize('json', DaySchedule.objects.all())
    return render(request=request, template_name='calendar.html', context={'dayschedules':dayschedules})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class DayScheduleViewSet(viewsets.ModelViewSet):
    queryset = DaySchedule.objects.all()
    serializer_class = DayScheduleSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


def testUI(request):
    users = django_serializers.serialize('json', User.objects.all())
    contacts = django_serializers.serialize('json', Contact.objects.all())
    departments = django_serializers.serialize('json', Department.objects.all())
    doctors = django_serializers.serialize('json', Doctor.objects.all())
    patients = django_serializers.serialize('json', Patient.objects.all())
    hospitals = django_serializers.serialize('json', Hospital.objects.all())
    return render(request=request, template_name='testUI.html',
                  context={'users':users,
                           'contacts':contacts,
                           'departments':departments,
                           'doctors':doctors,
                           'patients':patients,
                           'hospitals':hospitals,})
