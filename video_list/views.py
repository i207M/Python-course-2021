from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render

from .models import Video
from utils.err_handler import err_404
from utils.pagination import get_pagination_text


def index(request: HttpRequest):
    video_list = Video.objects.all()
    paginator = Paginator(video_list, 10)

    try:
        current_page_num = int(request.GET.get('page', 1))
        current_page = paginator.page(current_page_num)
    except Exception:
        return err_404(request, 'Invalid Page Num')

    pagination_text = get_pagination_text(current_page_num, paginator.num_pages)
    return render(request, 'video_list/index.html', locals())


def show(request: HttpRequest, aid: str):
    try:
        aid = int(aid)
        video = Video.objects.get(aid=aid)
        assert (video is not None)
    except Exception:
        return err_404(request, 'Invalid Video AID')

    return render(request, 'video_list/show.html', locals())
