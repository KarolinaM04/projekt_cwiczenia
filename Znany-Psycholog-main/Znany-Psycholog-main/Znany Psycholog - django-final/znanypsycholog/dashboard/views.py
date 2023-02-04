from django.shortcuts import render
from django.http import HttpResponse



def index(request):

    return HttpResponse(render(request, 'index.html'))

def login_page(request):
    return render(request, 'login-page.html')

def after_login(request):
    return HttpResponse(render(request, 'cennik.html'))

#BM
def forum(request):
    return HttpResponse(render(request, 'forum.html'))


def main_view(request):
    render(request, 'index.html')