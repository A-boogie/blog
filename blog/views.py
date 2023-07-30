from django.views.generic import ListView, DetailView
from .models import Post


# to display contents of the Post model using ListView


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
