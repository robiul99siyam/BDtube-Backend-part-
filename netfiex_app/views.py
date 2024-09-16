import urllib.error
import urllib.request
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import categoryModel, contentModel, ReviewModel, Playlist, Like,VideoWatchTime
from .serializer import categorySerializer, contentSerializer, reviewSeriailzer, PlayListSerializer, LikeSerilizer,VideoWatchSerializer
from rest_framework import filters
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from django.contrib.auth.models import User
import json,urllib
from ipware import get_client_ip

class LoctionTrack(APIView):
    def get(self,request,format=None):
        client_ip , is_routable = get_client_ip(request)
        if client_ip is None:
            client_ip = "0.0.0.0"
        else:
            if is_routable:
                is_type = "public"
            else:
                is_type = "private"
        print(client_ip,is_type)
        try:
            ip_address = "103.81.207.0"
            url = f"https://api.ipfind.com/?ip={ip_address}"
            response = urllib.request.urlopen(url)
            data = json.load(response)
            data['client_ip'] = client_ip
            data['is_type'] = is_type
            return Response(data)
        except urllib.error.URLError as e:
            return Response({"error" : str(e)}, status=500)





class CategoryViewsets(APIView):
    @method_decorator(cache_page(15))
    def get(self, request, pk=None, format=None):
        if pk is None:
            data = categoryModel.objects.all()
            serializer = categorySerializer(data, many=True)
            return Response(serializer.data)
        else:
            category = get_object_or_404(categoryModel, pk=pk)
            serializer = categorySerializer(category)
            return Response(serializer.data)

    @method_decorator(csrf_exempt)
    def post(self, request, format=None):
        serializer = categorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        category = get_object_or_404(categoryModel, pk=pk)
        serializer = categorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = get_object_or_404(categoryModel, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ContentViewSet(viewsets.ModelViewSet):
    # queryset = contentModel.objects.select_related('category', 'author').prefetch_related('view_count').only('id', 'title', 'description', 'category', 'author', 'view_count').all()
    queryset = contentModel.objects.select_related('category', 'author').prefetch_related(Prefetch('view_count', queryset=User.objects.all())).all()
    serializer_class = contentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.is_authenticated:
            self.update_view_count(instance, request.user)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def update_view_count(self, instance, user):
      
        if user not in instance.view_count.all():
            instance.view_count.add(user)
            instance.save(update_fields=['view_count'])

class ReviewViewsets(viewsets.ModelViewSet):
    queryset = ReviewModel.objects.select_related("user", "content").prefetch_related(
        Prefetch("user", queryset=User.objects.all()),
        Prefetch("user", queryset=User.objects.all())
    ).all()
    # queryset = ReviewModel.objects.all()
    serializer_class = reviewSeriailzer

    @method_decorator(cache_page(60 * 60 * 2))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class PlaylistViewsets(viewsets.ModelViewSet):
    queryset = Playlist.objects.select_related("user").all()
    serializer_class = PlayListSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60))
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class LikeViewset(APIView):

    @method_decorator(cache_page(60 * 60))
    def get(self, request, video_id=None):
        if video_id:
            like = Like.objects.filter(content_id=video_id).all()
        else:
            like = Like.objects.all()
        serializer = LikeSerilizer(like, many=True)
        return Response(serializer.data)

    @method_decorator(cache_page(60 * 60))
    def post(self, request, video_id=None):
        serializer = LikeSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save(content_id=video_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VideoWatchTimeViewset(APIView):

    def get(self,request,pk=None):
        if pk is None:
            data = VideoWatchTime.objects.all()
            serializer = VideoWatchSerializer(data,many=True)
            return Response(serializer.data)
        else:
            VideoWatchtime =  VideoWatchTime.objects.all()
            serializer = VideoWatchSerializer(VideoWatchtime)
            return Response(serializer.data)
        
    def post(self,request,format=None):
        serializer = VideoWatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
