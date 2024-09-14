from django.shortcuts import render
from .serializer import UserRegister,UserLogin,ImageSeralizer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from rest_framework.authtoken.models import Token
from .models import ImageUser

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers


class UserRegisterViewset(APIView):
    serializer_class  = UserRegister

    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Account Create Successfully")
        
        return Response(serializer.errors)

    # def get(self,request,format=None):
    #     users = User.objects.all()
    #     serializer = UserRegister(users,many=True)
    #     return Response(serializer.data)


class ImageViewset(viewsets.ModelViewSet):
    queryset = ImageUser.objects.select_related("user").all()
    serializer_class = ImageSeralizer
    
    def get_serializer_context(self):
        return {'request': self.request}
    # def get(self,request,format=None):
    #     image  = ImageUser.objects.all()
    #     serailzer = ImageSeralizer(image,many=True)
    #     return Response(serailzer.data)



class Userloginviews(APIView):

    @method_decorator(cache_page(60*60*2))
    def post(self,request):
        serializer = UserLogin(data= self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username,password=password)

            if user:
                token,_= Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request,user)
                return Response({'token':token.key,'user_id':user.id})
            else:
                return Response({"errors":"Invalid Data"})
        else:
            return Response(serializer.errors) 