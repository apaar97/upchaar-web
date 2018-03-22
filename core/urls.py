from django.urls import path, re_path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
# router.register(r'roles', views.RoleViewSet)
router.register(r'address', views.AddressViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'doctors', views.DoctorViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'hospitals', views.HospitalViewSet)
router.register(r'dayschedule', views.DayScheduleViewSet)
router.register(r'appointment', views.AppointmentViewSet)

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup/patient', views.signup_patient, name='signup_patient'),
    path('signup/doctor', views.signup_doctor, name='signup_doctor'),
    path('signup/hospital', views.signup_hospital, name='signup_hospital'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/docs/', include_docs_urls(title='UPCHAAR API', public=False)),
    path('api/login/', views.api_login, name='api_login'),
    path('api/logout/', views.api_logout, name='api_logout'),
    path('api/auth-token/', views.get_auth_token, name='api_auth_token'),
]
