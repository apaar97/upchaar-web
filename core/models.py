from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# class Role(models.Model):
#     PATIENT = 1
#     DOCTOR = 2
#     HOSPITAL = 3
#     ADMIN = 4
#     ROLE_CHOICES = (
#         (PATIENT, 'Patient'),
#         (DOCTOR, 'Doctor'),
#         (HOSPITAL, 'Hospital'),
#         (ADMIN, 'Admin'),
#     )
#     id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
#
#     def __str__(self):
#         return self.get_id_display()


class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.IntegerField()

    class Meta:
        unique_together = (('street', 'city', 'state', 'country', 'pincode'),)


class User(AbstractUser):
    PATIENT = 1
    DOCTOR = 2
    HOSPITAL = 3
    ADMIN = 4
    ROLE_CHOICES = (
        (PATIENT, 'Patient'),
        (DOCTOR, 'Doctor'),
        (HOSPITAL, 'Hospital'),
        (ADMIN, 'Admin'),
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    contact_no = models.IntegerField()

    def __str__(self):
        return self.contact_no


class Department(models.Model):
    department_name = models.CharField(max_length=50)
    department_desc = models.CharField(max_length=500)

    def __str__(self):
        return self.department_name


class Education(models.Model):
    education_desc = models.CharField(max_length=500)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.ManyToManyField(Department)
    education = models.OneToOneField(Education, on_delete=models.CASCADE)
    time_slot = models.DurationField()

    def __str__(self):
        return self.user.get_full_name()


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    patient_desc = models.CharField(max_length=500)

    def __str__(self):
        return self.user.get_full_name()


class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hospital_desc = models.CharField(max_length=500)

    def __str__(self):
        return self.user.get_full_name()


class DaySchedule(models.Model):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    DAYS = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    day = models.PositiveSmallIntegerField(choices=DAYS)
    time_slot_from = models.TimeField()
    time_slot_to = models.TimeField()


class Appointment(models.Model):
    CONFIRMED = 1
    CANCELLED = 2
    WAITING = 3
    STATUS_CODES = (
        (CONFIRMED, 'Confirmed'),
        (CANCELLED, 'Cancelled'),
        (WAITING, 'Waiting'),
    )
    appointment_date = models.DateField()
    time_slot_from = models.TimeField()
    token_no = models.IntegerField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CODES)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
