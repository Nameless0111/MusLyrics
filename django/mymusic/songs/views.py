from django.shortcuts import render, get_object_or_404, redirect
from .models import Song
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def song_list(request):
    query = request.GET.get('q')
    if query:
        songs = Song.objects.filter(Q(title__icontains=query) | Q(artist__icontains=query))
    else:
        songs = Song.objects.all()
    songs = songs.order_by('artist', 'title')
    return render(request, 'songs/song_list.html', {'songs': songs})

def song_detail(request, id):
 song = get_object_or_404(Song, id=id)
 return render(request, 'songs/song_detail.html', {'song': song})

def home(request):
 if request.user.is_authenticated:
     return redirect('song_list')
 else:
     return redirect('login')