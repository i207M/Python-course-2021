from django.shortcuts import redirect


def redirect_video_list(request):
    return redirect('/video_list/')
