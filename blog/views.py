from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # the default is blog/post_list.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # from latest to oldest
    # we can also specify the query set we want to display as a list
    # queryset = Post.objects.filter(title='First Post')  posts with title 'First Post'
    #  .. the default gives us all the posts


class PostDetailView(DetailView):  # the default template is blog/post_detail.html
    model = Post
    # the default object context passed is 'object' to be used on the template


# the LoginRequiredMixin doing the functionality of the loginrequired decorator for methods
# and it is used with class based views and passed as the first class
class PostCreateView(LoginRequiredMixin, CreateView):  # the template for this view is modelName_form ( post_form.html )
    model = Post
    fields = ['title', 'content']

    # this method is used to assign fields automatically
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # this method is used to assign fields automatically
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # this function is required by the UserPassesTestMixin and should return true if the
    # user trying to edit the post is the same user that wrote it
    def test_func(self):
        return self.request.user == self.get_object().author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # send them to the home page

    def test_func(self):
        return self.request.user == self.get_object().author



def about(request):
    return render(request, 'blog/about.html')

