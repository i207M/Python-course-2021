from django.shortcuts import render
from django.http import HttpRequest, HttpResponseNotFound
from django.core.paginator import Paginator

from .models import Video
from utils.pagination import get_pagination_text


def index(request: HttpRequest):
    video_list = Video.objects.all()
    paginator = Paginator(video_list, 10)

    current_page_num = int(request.GET.get('page', 1))
    if current_page_num not in paginator.page_range:
        return HttpResponseNotFound('<h1>Invalid Page Num</h1>')

    current_page = paginator.page(current_page_num)
    pagination_text = get_pagination_text(current_page_num, paginator.num_pages)

    return render(request, 'video_list/index.html', locals())


def show(request: HttpRequest, aid: str):
    aid = int(aid)
    video = Video.objects.get(aid=aid)
    if video is None:
        return HttpResponseNotFound('<h1>Invalid Video AID</h1>')

    return render(request, 'video_list/show.html', locals())
