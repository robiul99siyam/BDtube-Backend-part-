from .models import categoryModel,contentModel,ReviewModel ,Like,Playlist,VideoWatchTime
from rest_framework import serializers
from django.contrib.auth.models import User

# this category in serializer 
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']



class VideoWatchSerializer(serializers.ModelSerializer):
    # video = serializers.PrimaryKeyRelatedField(qureyset=VideoWatchTime.objects.all(),read_only=True)
    class Meta:
        model = VideoWatchTime
        fields = ['video','start_time','end_time','watch_time']
   



class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categoryModel
        fields = '__all__'
    

# this content serializers   

# this is review serializers 
class reviewSeriailzer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = ReviewModel
        fields = ['id','user','username', 'content', 'comment', 'datePosted']

class contentSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=categoryModel.objects.all(), write_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    author_username = serializers.CharField(source='author.username', read_only=True)
    author_id = serializers.CharField(source='author.id', read_only=True)
    total_views = serializers.SerializerMethodField()
    total_likes = serializers.IntegerField(source="like.count", read_only=True)
    reivew_content = reviewSeriailzer(many=True, read_only=True)

    class Meta:
        model = contentModel
        fields = [
            'id', 
            'category', 
            'category_name',  
            'author', 
            'author_username', 
            'author_id', 
            'title', 
            'language', 
            'videofile', 
            'thumbell', 
            'release_date',
            'description', 
            'total_views', 
            'total_likes', 
            'reivew_content'
        ]

    def get_total_views(self, obj):
        return obj.total_view_count()

    # def get_thumbell(self, obj):
    #     if obj.thumbell:
    #         return obj.thumbell.url
    #     return None


class LikeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'




class PlayListSerializer(serializers.ModelSerializer):
    content = serializers.PrimaryKeyRelatedField(queryset=contentModel.objects.all(), many=True, write_only=True)
    content_title = serializers.SerializerMethodField()

    class Meta:
        model = Playlist
        fields = ['id', 'user', 'list_name', 'content', 'content_title']

    def get_content_title(self, obj):
        request = self.context.get('request')
        return [{
            "id": content.id,
            "title": content.title,
            "thumbell": request.build_absolute_uri(content.thumbell.url) if content.thumbell else None,
        } for content in obj.content.all()]
