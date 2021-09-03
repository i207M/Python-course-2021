from django.shortcuts import render
from django.http import HttpResponse

from .models import Video


def index(request):
    context = {'page_num': 1, 'videos': Video.objects.filter(id__gte=1, id__lte=10)}
    return render(request, 'video_list/index.html', context=context)
