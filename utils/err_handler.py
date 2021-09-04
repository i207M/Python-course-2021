from django.shortcuts import render


def err404(request, err_msg: str = 'Not Found'):
    return render(request, '404.html', {'err_msg': err_msg}, status=404)
