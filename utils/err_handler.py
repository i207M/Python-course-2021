from django.shortcuts import render


def err404(request, err_msg: str = '404 Not Found'):
    return render(request, '404.html', context={'err_msg': err_msg}, status=404)
