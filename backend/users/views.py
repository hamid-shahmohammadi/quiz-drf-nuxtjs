from django.http import response
from rest_framework import views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt,datetime
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework.reverse import reverse
import requests
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny



class RegisterView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = get_user_model().objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found!')
    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Incorrect Password!')
    
    response = Response()
    
    token_endpoint = reverse(viewname='token_obtain_pair', request=request)
    tokens = requests.post(token_endpoint, data=request.data).json()
    
    response.data = {
        'access_token': tokens.get('access'),
        'refresh_token': tokens.get('refresh'),
        'email': user.email
    }
    
    return response

class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']

        user=User.objects.filter(email=email).first()
        serializer = UserSerializer(user)

        if user is None:
            raise AuthenticationFailed('user not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload={
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }

        token = jwt.encode(payload,'secret',algorithm='HS256')

        response=Response()

        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data={
            # 'jwt':token,
            'user':serializer.data
        }    

        return response

class UserView(APIView):
    def get(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('unauthenticated!')

        try:
            payload=jwt.decode(token,'secret',algorithms='HS256')
            print(payload['id'])  

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('unauthenticated!')

        user=User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):
    def post(self,request):
        response =Response()
        response.delete_cookie('jwt')
        response.data  = {
            'message':'success'
        } 
        return response  

class CurrentLoggedInUser(ModelViewSet):
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer
    
    def retrieve(self, request, *args, **kwargs):
        user_profile = self.queryset.get(email=request.user.email)
        serializer = self.get_serializer(user_profile)
        return Response({'user': serializer.data})                 

