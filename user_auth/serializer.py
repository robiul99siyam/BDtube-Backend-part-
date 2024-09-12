from rest_framework import serializers
from django.contrib.auth.models import User

from django.conf import settings
from rest_framework import serializers
from .models import ImageUser


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email']



class ImageSeralizer(serializers.ModelSerializer):
    user = userSerializer()
    

    class Meta:
        model = ImageUser
        fields = "__all__"

    # def get_image_url(self, obj):
    #     if obj.image:
    #         return obj.image.url
    #     return None

class UserRegister(serializers.ModelSerializer):
    confrim_password = serializers.CharField(required=True)
    image = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','confrim_password','email',"image"]
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        email = self.validated_data['email']
        last_name = self.validated_data['last_name']
        password = self.validated_data['password']
        pasword1 = self.validated_data['confrim_password']
        image = self.validated_data.get('image') 

        if password != pasword1:
            raise serializers.ValidationError(
                {
                    "errors": "Passwords don't match"
                }
            )
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {
                    "errors": "Email already exists"
                }
            )

        account = User(username=username, first_name=first_name, last_name=last_name, email=email)
        account.set_password(password)
        # account.is_active = False
        account.save()
        
        
        if image:
            ImageUser.objects.create(user=account,image=image)
        return account





class UserLogin(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)