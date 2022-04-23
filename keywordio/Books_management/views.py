from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required

from Books_management.forms import BookModelForm, CategoryModelForm, LoginForm
from .models import *
from django.db.models import Q

from django.contrib import messages


def index(request):
   
    files = Resume_download_file.objects.all()

    return render(request, 'index.html', {'files': files})


def library(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    book_count = books.count()

    active_category = request.GET.get('category', '')

    if active_category:
        books = books.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        books = books.filter(Q(name__icontains=query) |
                             Q(description__icontains=query) | Q(author__icontains=query) | Q(slug__icontains=query))

    context = {
        'categories': categories,
        'books': books,
        'active_category': active_category,
        'book_count':book_count
    }

    return render(request, 'library.html', context)


def book(request, slug):
    book = get_object_or_404(Book, slug=slug)

    return render(request, 'book.html', {'book': book})


def create_category(request):
    form = CategoryModelForm()

    if request.method == 'POST':
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('create_book')

    else:
        form = CategoryModelForm()
    return render(request, 'create_category.html', {'form': form})


def create_book(request):

    form = BookModelForm()

    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('library')

    else:
        form = BookModelForm()

    return render(request, 'create_book.html', {'form': form})


def update_book(request , id):
    
    s = Book.objects.get(id=id)

    form = BookModelForm(instance=s)

    dict = {'form': form}
    
    
    if request.method == 'POST':
        form = BookModelForm(request.POST,request.FILES,instance=s)
        if form.is_valid():
            form.save()

        return redirect('library')


    return render(request, 'update_book.html', dict)


def delete_book(request , id):
    
    book_obj = Book.objects.get(id=id)

    book_obj.delete()


    return redirect('library')



def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')

            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Email id already exists')
                return redirect('register')

            else:
                user = CustomUser.objects.create_user(
                    username=username, email=email, password=password1)
                user.is_superuser = True
                user.is_staff = True
                user.save()

                print('User Created')
                return redirect('login')

        else:
            messages.info(request, 'password must match')
            return redirect('register')

    else:

        return render(request, 'accounts/admin_signup.html')

from django.contrib.auth import views as auth_views


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


def logout(request):
    CustomUser.logout(request)
    return redirect('/')


def Files(request):

    files = Resume_download_file.objects.all()

    return render(request, 'resume.html', {'files': files})