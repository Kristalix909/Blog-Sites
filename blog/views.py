from email import message
import re
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post   
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


class PostList(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post_list.html'

# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'blog/post_list.htm', {'posts': posts, 'page': page})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post_detail.html', {'post': post})


def registration(request):
    if request.user.is_authenticate:
        return redirect('home')
    else:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request,user)
                message.success(request,' Muvaffaqiyatli royihatdan otdingiz!')
                return redirect('home')
            message.error(request, 'Malumotlar xato toldirilgan!')
        return render(request, 'blog/register.html', {'register_form': form})