from django.shortcuts import render,get_object_or_404

from .models import Meeting

def detail(request, id):
    meeting = Meeting.objects.get(pk=id)
    return render(request, "meetings/detail.html", {"meeting": meeting})
def detail(request, id):
    meeting = get_object_or_404(Meeting,id)
    return render(request, "meetings/detail.html", {"meeting": meeting})