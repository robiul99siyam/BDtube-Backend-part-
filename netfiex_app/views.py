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
    # queryset = contentModel.objects.all()
    queryset = contentModel.objects.select_related('category', 'author').prefetch_related('view_count').all()
    serializer_class = contentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.user.is_authenticated:
            instance.view_count.add(request.user)

        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ReviewViewsets(viewsets.ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = reviewSeriailzer

    @method_decorator(cache_page(60 * 60 * 2))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

class PlaylistViewsets(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
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
