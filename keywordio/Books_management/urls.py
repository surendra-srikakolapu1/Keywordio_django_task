from django.urls import path, include,re_path
from .views import *

from django.conf import settings

from .views import Files
from django.views.static import serve


urlpatterns = [
    path('', index, name="index"),
    path('library/', library, name='library'),
    path('library/<slug:slug>/', book, name='book'),

    path('create_book/', create_book, name='create_book'),
    path('update_book/<int:id>/', update_book, name='update_book'),
    path('delete_book/<int:id>/', delete_book, name='delete_book'),



    path('create_category/', create_category, name='create_category'),


    path('register/', register, name='register'),
    path('logout', logout, name='logout'),
    path('accounts/signout/', register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('login/', LoginView.as_view(), name='login'),


    path('file', Files, name='download-list'),
    re_path
    (r'download/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),


]
