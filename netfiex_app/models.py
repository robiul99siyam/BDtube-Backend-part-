from django.db import models
from django.contrib.auth.models import User


from django.utils import timezone
# this is categroy field and relation foreginkey 
class categoryModel(models.Model):
    name = models.CharField(max_length=250)
   
    def __str__(self):
        return f"this is categroy - {self.name}"
    




LANGUAGE = [
    ("Bangla","Bangla"),
    ("English","English"),
    ("Handi","Handi"),
    
]

# this content model 


class contentModel(models.Model):
    category = models.ForeignKey(categoryModel, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=250)
    release_date = models.DateField(auto_now_add=True)
    language = models.CharField(choices=LANGUAGE, max_length=20)
    videofile = models.FileField(upload_to='video/', null=True, blank=True)  
    thumbell = models.ImageField(upload_to='image', null=True, blank=True) 
    view_count = models.ManyToManyField(User, related_name="content_view")
    description = models.TextField(null=True)

    def __str__(self):
        return f" this is title -  {self.title} "

    def total_view_count(self):
        return self.view_count.count()




class ReviewModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    content = models.ForeignKey(contentModel,on_delete=models.CASCADE,null=True,related_name="reivew_content")
    comment = models.TextField()
    datePosted = models.DateField(auto_now_add=True)

    




class Like(models.Model):
    user = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE)
    content = models.ForeignKey(contentModel,related_name="like",on_delete=models.CASCADE)
    liked_at = models.DateField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'content') 






class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)



class Playlist(models.Model):
    list_name = models.CharField(max_length=250,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    content = models.ManyToManyField(contentModel)





class VideoWatchTime(models.Model):
    video = models.ForeignKey(contentModel,on_delete=models.CASCADE,null=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True,blank=True)
    watch_time = models.DurationField(null=True,blank=True)

    def save(self,*args,**kwargs):
        if self.end_time and not self.watch_time:
            self.watch_time = self.end_time - self.start_time
        super().save(*args,**kwargs)





