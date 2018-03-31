from django.utils import timezone
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User, Contact, Department, Doctor, Patient, Hospital, DaySchedule, Appointment, Notification


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Contact
        fields = ('url', 'id', 'user', 'contact_no',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, style={'input_type': 'password'})
    contacts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='contact_no'
    )

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'first_name', 'last_name', 'password', 'gender', 'date_of_birth',
                  'role', 'contacts')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('url', 'id', 'department_name',)


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    department = serializers.SlugRelatedField(
        queryset=Department.objects.all(),
        slug_field='department_name'
    )

    class Meta:
        model = Doctor
        fields = ('url', 'user', 'department', 'education', 'time_slot',)


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Patient
        fields = ('url', 'user',)


class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Hospital
        fields = ('url', 'user', 'hospital_name', 'no_of_beds', 'latitude', 'longitude')


class DayScheduleSerializer(serializers.HyperlinkedModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    hospital = serializers.PrimaryKeyRelatedField(queryset=Hospital.objects.all())

    class Meta:
        model = DaySchedule
        fields = ('url', 'id', 'doctor', 'hospital', 'day', 'time_slot_from', 'time_slot_to')


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    hospital = serializers.PrimaryKeyRelatedField(queryset=Hospital.objects.all())

    class Meta:
        model = Appointment
        fields = ('url', 'id', 'patient', 'doctor', 'hospital', 'appointment_date', 'time_slot_from',
                  'status', 'token_no')


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ('url', 'id', 'user_id', 'message')
