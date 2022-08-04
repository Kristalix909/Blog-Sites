########################IMPORT########################
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post   
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

########################RESERVE########################
# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.contrib import messages
# from .forms import RegisterForm

########################POSTS########################
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


########################POST DETAIL########################
def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post_detail.html', {'post': post})

########################REGISTRATION########################

# def registration(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         form = RegisterForm()
#         if request.method == 'POST':
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 user = form.save()
#                 login(request,user)
#                 message.success(request,' Muvaffaqiyatli royihatdan otdingiz!')
#                 return redirect('home')
#             message.error(request, 'Malumotlar xato toldirilgan!')
#         return render(request, 'blog/register.html', {'register_form': form})

########################AUTHENTICATE########################
def registration(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    print("Such a username already exists")
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    print("Such a email already exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    login(request, user)
                    return redirect('post_list')
            else:
                print("Passwords are not the same")
                return redirect('register')
        else:
            return render(request, 'blog/register.html')

########################LOG OUT########################
def logoutUser(request):
    logout(request)
    return redirect('post_list')


########################LOG IN########################
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_list')
            else:
                print('Username or password error')
                return redirect('login')
        else:
            return render(request, 'blog/login.html')