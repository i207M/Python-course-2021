from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator

from up_list.models import Up
from video_list.models import Video
from utils.pagination import get_pagination_text
from utils.err_handler import err404


def search_video(request: HttpRequest):
    search_text = request.GET.get('query', '')
    up_list = Up.objects.all()
    paginator = Paginator(up_list, 10)

    try:
        current_page_num = int(request.GET.get('page', 1))
        assert (current_page_num in paginator.page_range)
    except Exception:
        return err404(request, 'Invalid Page Num')

    current_page = paginator.page(current_page_num)
    pagination_text = get_pagination_text(current_page_num, paginator.num_pages)

    return render(request, 'search/index.html', locals())


def search_up(request: HttpRequest):
    pass


def index(request: HttpRequest):
    if not request.GET.get('query'):
        return render(request, 'search/base.html')
    elif request.GET.get('up') == 'on':
        return search_up(request)
    else:
        return search_video(request)
