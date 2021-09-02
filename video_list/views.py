from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'videos': [
            {
                'title': 'A',
                'desc': 'B',
            },
        ]
    }
    return render(request, 'video_list/index.html', context=context)
