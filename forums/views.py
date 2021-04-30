from django.shortcuts import render

from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' #use post.author instead of object.author
    ordering = ['-date_posted'] #for ordering accoing to date
    paginate_by = 10 #buit in paginator function

    def get_context_data(self,**kwargs):
        context = super(PostListView,self).get_context_data(**kwargs)
        context['title'] = "Health Blog"
        return context


class PostDetailView(DetailView):
    model = Post

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content'] #form fields

    def form_valid(self, form):
        #form<this form> <set author> = current logged in user
        form.instance.author = self.request.user
        #run overridden form_valid method
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content'] #form fields

    def form_valid(self, form):
        #form<this form> <set author> = current logged in user
        form.instance.author = self.request.user
        #run overridden form_valid method
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
