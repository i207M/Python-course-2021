from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from .models import Video


def index(request):
    video_list = Video.objects.all()
    paginator = Paginator(video_list, 10)

    current_page_num = int(request.GET.get('page', 1))
    current_page = paginator.page(current_page_num)
    return render(request, 'video_list/index.html', locals())
