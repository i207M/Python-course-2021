from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator

from .models import Video
from utils.pagination import get_pagination_text, err404


def index(request: HttpRequest):
    video_list = Video.objects.all()
    paginator = Paginator(video_list, 10)

    try:
        current_page_num = int(request.GET.get('page', 1))
        assert (current_page_num in paginator.page_range)
    except Exception:
        return err404(request, 'Invalid Page Num')

    current_page = paginator.page(current_page_num)
    pagination_text = get_pagination_text(current_page_num, paginator.num_pages)

    return render(request, 'video_list/index.html', locals())


def show(request: HttpRequest, aid: str):
    try:
        aid = int(aid)
        video = Video.objects.get(aid=aid)
        assert (video is not None)
    except Exception:
        return err404(request, 'Invalid Video AID')

    return render(request, 'video_list/show.html', locals())
