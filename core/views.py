from django.conf import settings
from django.contrib.auth import login, authenticate
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, detail_route, list_route
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK
from rest_framework.authtoken.models import Token
from .models import User
from django.shortcuts import render


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

def options(request):
    return render(request, 'options.html')

#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
