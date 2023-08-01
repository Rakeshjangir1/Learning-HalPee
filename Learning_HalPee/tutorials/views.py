from django.shortcuts import render
from django.shortcuts import redirect
from .models.chapters import chapter, html_post, css_post
# Create your views here.



def index(request):
    return redirect('html/')

def html(request):
    post_info = html_post.objects.filter(status=1)
    dict = {'post_info':post_info}
    return render(request, 'detailspage.html', dict)

def html_details(request,slug):
    post_info = html_post.objects.filter(status=1)
    if request.method == 'GET':
        if html_post.objects.filter(slug=slug).exists():
            content = html_post.objects.filter(slug=slug, status=1)
            for data in content:
                content = data.content
    dict = {'post_info':post_info,
            'content':content,}
    return render(request, 'detailspage.html', dict)


def css(request):
    post_info = css_post.objects.filter(status=1)
    dict = {'post_info':post_info}
    return render(request, 'detailspage.html', dict)

def css_details(request,slug):
    post_info = css_post.objects.filter(status=1)
    if request.method == 'GET':
        if css_post.objects.filter(slug=slug).exists():
            content = css_post.objects.filter(slug=slug, status=1)
            for data in content:
                content = data.content
    dict = {'post_info':post_info,
            'content':content,}
    return render(request, 'detailspage.html', dict)





def javascript(request):
    return render(request, 'detailspage.html')

def bootstrap(request):
    return render(request, 'detailspage.html')

def python(request):
    return render(request, 'detailspage.html')

