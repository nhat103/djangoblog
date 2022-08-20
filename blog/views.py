from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Post

# Create your views here.


def post_list(request):
    post = Post.publish.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

    # after all try a test
  #  post = Post.publish.all()
  #  template = loader.get_template('blog/post/list.html')
   # return HttpResponse(template.render(), {'post': posts})


def post_detail(request, year, month, day, posts):
    post = get_object_or_404(Post, slug=post, status='pushlish',
                             publish_year=year, publish_month=month, publish_day=day)
    template = loader.get_template('blog/post/detail.html', {'posts': posts})
    return HttpResponse(template.render())
