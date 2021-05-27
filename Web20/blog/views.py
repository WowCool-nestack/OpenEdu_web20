from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def blog_home(request):
    blog = Articles.objects.order_by('-date')
    return render(request, 'blog/blog_home.html', {'blog': blog})


class BlogDetailView(DetailView):
    model = Articles
    template_name = 'blog/details_view.html'
    context_object_name = 'article'


def create(request):
    error=''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма неверно заполнена'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'blog/create.html', data)




