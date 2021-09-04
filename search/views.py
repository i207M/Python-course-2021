import time

from django.shortcuts import render
from django.http import HttpRequest
from django.core.paginator import Paginator

from up_list.models import Up
from video_list.models import Video
from utils.pagination import get_pagination_text
from utils.err_handler import err_404


def encode_params(GET) -> str:
    mutable_params = GET.copy()
    mutable_params.pop('page', None)
    return mutable_params.urlencode()


def search_video(request: HttpRequest):
    start_time = time.time()

    search_text = request.GET.get('query', '')
    video_list = Video.objects.filter(title__contains=search_text
                                      ) | Video.objects.filter(desc__contains=search_text)
    paginator = Paginator(video_list, 10)

    try:
        current_page_num = int(request.GET.get('page', 1))
        assert (current_page_num in paginator.page_range)
    except Exception:
        return err_404(request, 'Invalid Page Num')

    current_page = paginator.page(current_page_num)
    params_encoded = encode_params(request.GET)
    pagination_text = get_pagination_text(current_page_num, paginator.num_pages, params_encoded)

    time_usage = f'{time.time() - start_time:.3f}'

    return render(request, 'search/video.html', locals())


def search_up(request: HttpRequest):
    start_time = time.time()

    search_text = request.GET.get('query', '')
    up_list = Up.objects.filter(name__contains=search_text
                                ) | Up.objects.filter(sign__contains=search_text)
    paginator = Paginator(up_list, 10)

    try:
        current_page_num = int(request.GET.get('page', 1))
        assert (current_page_num in paginator.page_range)
    except Exception:
        return err_404(request, 'Invalid Page Num')

    current_page = paginator.page(current_page_num)
    params_encoded = encode_params(request.GET)
    pagination_text = get_pagination_text(current_page_num, paginator.num_pages, params_encoded)

    time_usage = f'{time.time() - start_time:.3f}'

    return render(request, 'search/up.html', locals())


def index(request: HttpRequest):
    cat = request.GET.get('category')
    if cat is None or not request.GET.get('query'):
        return render(request, 'search/base.html', locals())
    elif cat == 'video':
        return search_video(request)
    else:
        return search_up(request)
