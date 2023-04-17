#THIRD_PARTY_APPS
from firebase_admin import auth
#rest_framework
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
#django import
from django.views.generic import TemplateView
#
from .models import User

#
from .serializers import (
    UserSerializer,
    LoginSocialSerializer
)


class LoginUser(TemplateView):
    template_name = "users/login.html"


class GoogleLoginView(APIView):
    """
        para iniciar sesion co una cuenta google
    """

    serializer_class = LoginSocialSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        print('===========', 'post execute')
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        # serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            print('todo muy bien')
        else:
            print(serializer.errors)
        #
        id_token = serializer.data.get('token_id')
        #
        print('=====', id_token)
        #
        return Response({
            'status': 'ok',
        })

# Create your views here.
