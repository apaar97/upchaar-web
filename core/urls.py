from django.urls import path, re_path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'doctors', views.DoctorViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'hospitals', views.HospitalViewSet)
router.register(r'dayschedule', views.DayScheduleViewSet)
router.register(r'appointment', views.AppointmentViewSet)
router.register(r'notifications', views.NotificationViewSet)

urlpatterns = [
    path('testUI/', views.testUI, name='testUI'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signup/patient', views.signup_patient, name='signup_patient'),
    path('signup/doctor', views.signup_doctor, name='signup_doctor'),
    path('signup/hospital', views.signup_hospital, name='signup_hospital'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/doctor', views.dashboard_doctor, name='dashboard_doctor'),
    path('dashboard/hospital', views.dashboard_hospital, name='dashboard_hospital'),
    path('appointment/book', views.book_appointment, name='book_appointment'),
    path('appointment/filter', views.filter_appointment, name='filter_appointment'),
    path('appointment/calendar', views.calendar_appointment, name='calendar_appointment'),
    path('appointment/upcoming', views.upcoming_appointment, name='upcoming_appointment'),
    path('doctor/leave', views.doctor_leave, name='doctor_leave'),
    path('doctor/leave/reschedule', views.doctor_leave_after, name='doctor_leave_after'),
    path('notifications', views.notifications, name='notifications'),
    path('faq', views.faq, name='faq'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/docs/', include_docs_urls(title='UPCHAAR API', public=False)),
    path('api/login/', views.api_login, name='api_login'),
    path('api/logout/', views.api_logout, name='api_logout'),
    path('api/auth-token/', views.get_auth_token, name='api_auth_token'),
    path('api/send-sms/', views.send_sms, name='api_send_sms'),
    path('api/send-notification/', views.send_notification, name='api_send_notification'),
]
