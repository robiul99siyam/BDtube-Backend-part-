from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter
# create router object
router = DefaultRouter()
# Register
router.register('image', views.ImageViewset)




urlpatterns = [
    path('profile/', include(router.urls)),
    path("account/create/",views.UserRegisterViewset.as_view(),name="register"),
    path("account/login/",views.Userloginviews.as_view(),name="login"),
]