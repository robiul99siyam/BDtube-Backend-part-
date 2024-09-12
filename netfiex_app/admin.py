from django.contrib import admin
from .models import categoryModel,contentModel,ReviewModel,Notification,Like,Playlist,VideoWatchTime



admin.site.register(categoryModel)
admin.site.register(contentModel)
admin.site.register(ReviewModel)
admin.site.register(Like)
admin.site.register(Playlist)
admin.site.register(VideoWatchTime)

