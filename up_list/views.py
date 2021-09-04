from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render

from .models import Up
from video_list.models import Video
from utils.err_handler import err_404
from utils.pagination import get_pagination_text


def index(request: HttpRequest):
    up_list = Up.objects.all()
    paginator = Paginator(up_list, 10)

    try:
        current_page_num = int(request.GET.get('page', 1))
        current_page = paginator.page(current_page_num)
    except Exception:
        return err_404(request, 'Invalid Page Num')

    pagination_text = get_pagination_text(current_page_num, paginator.num_pages)
    return render(request, 'up_list/index.html', locals())


def show(request: HttpRequest, id: str):
    try:
        id = int(id)
        up = Up.objects.get(id=id)
        assert (up is not None)
    except Exception:
        return err_404(request, 'Invalid UP ID')

    up_video_list = Video.objects.filter(up_id=id)
    paginator = Paginator(up_video_list, 10)

    try:
        current_page_num = int(request.GET.get('page', 1))
        current_page = paginator.page(current_page_num)
    except Exception:
        return err_404(request, 'Invalid Page Num')

    pagination_text = get_pagination_text(current_page_num, paginator.num_pages)
    return render(request, 'up_list/show.html', locals())
