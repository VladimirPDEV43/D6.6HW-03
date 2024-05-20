from django.views.generic import ListView, DetailView
from .models import *
from datetime import datetime


class PostList(ListView):
#   model = Post
#   ordering = 'header_post'
    queryset = Post.objects.order_by(
        '-time_of_publication'
    )
    template_name = 'flatpages/news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_pub'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
    pk_url_kwarg = 'id'
