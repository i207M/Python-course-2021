from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator

from .models import Video


def get_pagination_text(page: int, max_page: int) -> str:
    '''
    <li class="active pink lighten-2"><a href="#!">1</a></li>
    <li class="waves-effect"><a href="#!">2</a></li>
    <li class="disabled"><a href="#!"><i>...</i></a></li>
    '''
    page_list = []
    if page <= 4:
        for i in range(1, page + 3):
            page_list.append(i)
        page_list.append('...')
        page_list.append(max_page)
    elif max_page - page <= 3:
        page_list.append(1)
        page_list.append('...')
        for i in range(page - 2, max_page + 1):
            page_list.append(i)
    else:
        page_list.append(1)
        page_list.append('...')
        for i in range(page - 2, page + 3):
            page_list.append(i)
        page_list.append('...')
        page_list.append(max_page)

    ret = ''
    for p in page_list:
        if p == '...':
            ret += '<li class="disabled"><a href="#!"><i>...</i></a></li>'
        elif p == page:
            ret += f'<li class="active pink lighten-2"><a href="#!">{p}</a></li>'
        else:
            ret += f'<li class="waves-effect"><a href="?page={p}">{p}</a></li>'
    return ret


def index(request: HttpRequest):
    video_list = Video.objects.all()
    paginator = Paginator(video_list, 10)

    current_page_num = int(request.GET.get('page', 1))  # TODO
    current_page = paginator.page(current_page_num)
    pagination_text = get_pagination_text(current_page_num, paginator.num_pages)

    return render(request, 'video_list/index.html', locals())


def show(request: HttpRequest):
    aid = int(request.GET.get('id'))  # TODO
    video = Video.objects.get(aid=aid)
    return render(request, 'video_list/show.html', locals())
