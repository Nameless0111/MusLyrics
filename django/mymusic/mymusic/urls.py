from django.contrib import admin
from django.urls import include, path
from songs import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('songs.urls')),
    path('', views.home, name='home'),
    path('authors/', include('author.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]