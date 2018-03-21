from django.urls import path, re_path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/docs/', include_docs_urls(title='UPCHAAR API', public=False)),
    path('api/login/', views.api_login, name='api_login'),
    path('api/logout/', views.api_logout, name='api_logout'),
    path('api/auth-token/', views.get_auth_token, name='api_auth_token'),
    path('options/',views.options, name='options')
]
