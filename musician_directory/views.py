from django.shortcuts import render

from albums.models import Album





def home(request):
    album = Album.objects.all()
    return render(request,'home.html',{'data':album})




