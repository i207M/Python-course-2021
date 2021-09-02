from django.shortcuts import redirect


def redirector(request):
    return redirect('/video_list/')
