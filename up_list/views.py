from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator

from .models import Up
from video_list.models import Video
from utils.pagination import get_pagination_text, err404


def index(request: HttpRequest):
    up_list = Up.objects.all()
    paginator = Paginator(up_list, 10)

    try:
        current_page_num = int(request.GET.get('page', 1))
        assert (current_page_num in paginator.page_range)
    except Exception:
        return err404(request, 'Invalid Page Num')

    current_page = paginator.page(current_page_num)
    pagination_text = get_pagination_text(current_page_num, paginator.num_pages)

    return render(request, 'up_list/index.html', locals())


def show(request: HttpRequest, id: str):
    try:
        id = int(id)
        up = Up.objects.get(id=id)
        assert (up is not None)
    except Exception:
        return err404(request, 'Invalid UP ID')

    up_video_list = Video.objects.filter(up_id=id)
    paginator = Paginator(up_video_list, 10)

    current_page_num = int(request.GET.get('page', 1))
    current_page = paginator.page(current_page_num)
    pagination_text = get_pagination_text(current_page_num, paginator.num_pages)

    return render(request, 'up_list/show.html', locals())
