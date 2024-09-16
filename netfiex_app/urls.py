from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
# create router object
router = DefaultRouter()
# Register
# router.register('category', views.CategoryViewsets)
router.register("content", views.ContentViewSet)
router.register("review",views.ReviewViewsets)
router.register("playlist",views.PlaylistViewsets)


urlpatterns = [
    path('api/', include(router.urls)),
    path('video/<int:video_id>/like/', views.LikeViewset.as_view(), name='like-create'),
    path('category/', views.CategoryViewsets.as_view()),       
    path('category/<int:pk>/', views.CategoryViewsets.as_view()),
    path("videoWatch/",views.VideoWatchTimeViewset.as_view()),
    path("videoWatch/<int:pk>/",views.VideoWatchTimeViewset.as_view()),
    path("location/",views.LoctionTrack.as_view())
   

]