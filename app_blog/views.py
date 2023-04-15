from django.shortcuts import render
from .models import Post, Comment
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def blog_home(request):

    context = {}
    context['visitor_name'] = request.user
    return render(request, 'app_blog/home.html', context=context)


def blog_list(request):
    context = {}
    context['blogs'] = Post.objects.all()
    return render(request, 'app_blog/post_list.html', context=context)

class CommmentAddView(CreateView):
    model = Comment
    fields = '__all__'
    success_url = '/'


class PostCreateView(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/blog/list/'

    # Behind the scenes,
    # 1) form is automatically generated and accessible via {{ form }} in template
    # Error message included, previously submitted values in tact
    # Default server-side validation
    # Default client-side validation

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = '/blog/list/' # when a Post is successfully updated, redirect to this url


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/list/'


def blog_create(request):
    context = {}

    # Is the user just loading this page or submitting a form?
    # If the user is submitting the form
    if request.method == 'POST':

        # process the data
        
        input_title = request.POST.get('title')
        input_author = request.POST.get('author')
        input_content = request.POST.get('content')

        if input_title == '':
            context['error_message'] = 'Title must not be empty!'
            context['input_author'] = input_author
            context['input_content'] = input_content

        else:
            # API to create an object
            Post.objects.create(
                title=input_title,
                author=input_author,
                content=input_content,
            )

            return reverse('blog-create')

    return render(request, 'app_blog/post_create.html', context=context)


