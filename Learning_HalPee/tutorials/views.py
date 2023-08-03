from django.shortcuts import render
from django.shortcuts import redirect
from .models.chapters import chapter, html_post, css_post
# Create your views here.
from django.template.defaulttags import register

@register.filter(name='split')
def split(value, key):
    value.split("key")
    return value.split(key)



def index(request):
    return redirect('html/')

def html(request):
    path = request.path.split('/')
    post_info = html_post.objects.filter(status=1)

    # Redirect to first page of chapter
    if html_post.objects.filter(status=1).exists():
        post_info = html_post.objects.filter(status=1, id=1)
        for i in post_info:
            return redirect(str(request.path) + i.slug)

    # render data in dictionary for template from models
    dict = {'post_info':post_info,
            'path':path}
    return render(request, 'detailspage.html', dict)

def html_details(request,slug):
    path = request.path.split('/')

    #fetching Published data only
    post_info = html_post.objects.filter(status=1)
    if request.method == 'GET':
        if html_post.objects.filter(slug=slug).exists():
            content = html_post.objects.filter(slug=slug, status=1)
    dict = {'post_info':post_info,
            'content':content,
            'path':path}
    return render(request, 'detailspage.html', dict)


def css(request):
    path = request.path.split('/')
    post_info = css_post.objects.filter(status=1)

    # Redirect to first page of chapter
    if css_post.objects.filter(status=1).exists():
        css_info = html_post.objects.filter(status=1, id=1)
        for i in post_info:
            return redirect(str(request.path) + i.slug)

    # render data in dictionary for template from models
    dict = {'post_info':post_info,
            'path':path}
    return render(request, 'detailspage.html', dict)

def css_details(request,slug):
    path = request.path.split('/')

    #fetching Published data only
    post_info = css_post.objects.filter(status=1)
    if request.method == 'GET':
        if css_post.objects.filter(slug=slug).exists():
            content = css_post.objects.filter(slug=slug, status=1)
    dict = {'post_info':post_info,
            'content':content,
            'path':path}
    return render(request, 'detailspage.html', dict)





def javascript(request):
    path = request.path.split('/')
    dict = {'path':path}
    return render(request, 'detailspage.html', dict)

def bootstrap(request):
    path = request.path.split('/')
    dict = {'path':path}
    return render(request, 'detailspage.html', dict)

def python(request):
    path = request.path.split('/')
    dict = {'path':path}
    return render(request, 'detailspage.html', dict)

