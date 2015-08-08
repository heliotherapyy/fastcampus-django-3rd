from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Post

# from pystagram import settings
from django.conf import settings


def index(request):
    count = request.session.get('index_page_count', 0) + 1
    request.session['index_page_count'] = count

    post_list = Post.objects.all()

    return render(request, 'blog/index.html', {
        'count': count,
        'post_list': post_list,
    })


def detail(request, pk):
  # try:
  #     post = Post.objects.get(pk=pk)
  # except Post.DoesNotExist:
  #     raise Http404

    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/detail.html', {
        'post': post,
    })


    '''
    if int(pk) == 0:
        pass
    response = HttpResponse('page not found')
    response['X-Custom-Header'] = 'hello world'
    response.status_code = 404
    response.content_type = 'text/html'
    return response
    '''


