from django.conf import settings
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, reverse
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from rest_framework.authtoken.models import Token

from .models import User
from django.shortcuts import render
from .models import Address, User, Contact, Department, Education, Doctor, Patient, Hospital, DaySchedule, Appointment
from .serializers import *
from .forms import UserSignUpForm


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
    # if request.method == 'POST':
    #     userform = UserSignUpForm(request.POST)
    #     if userform.is_valid():
    #         user = userform.save()
    #         username = userform.cleaned_data.get('username')
    #         raw_password = userform.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return redirect('index')
    # else:
    #     userform = UserSignUpForm()
    # return render(request=request, template_name='signup/signup_user.html', context={'userform': userform})
    return render(request=request, template_name='signup/signup.html')


def signup_patient(request):
    return render(request=request, template_name='signup/signup_patient.html')


def signup_doctor(request):
    return render(request=request, template_name='signup/signup_patient.html')


def signup_hospital(request):
    return render(request=request, template_name='signup/signup_patient.html')


# class RoleViewSet(viewsets.ModelViewSet):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


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
