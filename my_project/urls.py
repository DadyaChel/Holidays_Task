from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from posts import views

router = routers.DefaultRouter()
router.register('tweet', views.TweetViewSet)
router.register('com', views.CommentViewSet)
router.register('like', views.LikeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', auth_views.obtain_auth_token),


    path('tweet/', views.TweetCreateListView.as_view()),
    path('tweet/<int:pk>/', views.TweetRetrieveUpdateDestroyAPIView.as_view()),

    path('com/', views.CommentListCreateAPIView.as_view()),
    path('com/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view()),

    path('like/', views.LikeCreateListView.as_view()),
    path('like/<int:pk>/', views.LikeRetrieveUpdateDestroyAPIView.as_view()),

    path('api/v-1.1/', include(router.urls)),
]