from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('signup.urls')),
    path('login/', include('login.urls')),
    path('tweet/', include('tweet.urls')),
    path('tweet_del/', include('tweet_del.urls')),
    path('user_auth/', include('user_auth.urls')),
]
