from django.utils import timezone
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Address, User, Contact, Department, Education, Doctor, Patient, Hospital, DaySchedule, Appointment


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('url', 'id', 'street', 'city', 'state', 'country', 'pincode',)


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Contact
        fields = ('url', 'id', 'user', 'contact_no',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, style={'input_type': 'password'})
    address = AddressSerializer()
    contacts = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='contact_no'
     )

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'first_name', 'last_name', 'password', 'gender', 'date_of_birth',
                  'role', 'address', 'contacts')
        write_only_fields = ('password',)
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        user = User.objects.create_user(**validated_data)
        Address.objects.create(user=user, **address_data)
        return user


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('url', 'id', 'department_name', 'department_desc',)


class EducationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Education
        fields = ('url', 'id', 'education_desc',)


class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    department = DepartmentSerializer(many=True)
    education = EducationSerializer()

    class Meta:
        model = Doctor
        fields = ('url', 'user', 'department', 'education', 'time_slot',)

    def create(self, validated_data):
        department_data = validated_data.pop('department')
        education_data = validated_data.pop('education')
        doctor = Doctor.objects.create_user(**validated_data)
        Department.objects.create(**department_data)
        Education.objects.create(**education_data)
        return doctor


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Patient
        fields = ('url', 'user', 'patient_desc',)


class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Hospital
        fields = ('url', 'user', 'hospital_desc',)


class DayScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DaySchedule
        fields = '__all__'


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
