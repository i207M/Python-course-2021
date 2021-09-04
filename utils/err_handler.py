from django.shortcuts import render


def err_404(request, err_msg: str = 'Not Found'):
    return render(request, '404.html', locals(), status=404)
