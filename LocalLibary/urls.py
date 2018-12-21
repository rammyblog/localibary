from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('libary/', views.index, name='index'),
    path('libary/books/',views.BookList.as_view(), name='book_list'),
    path('libary/book/<int:pk>', views.bookDetails, name='book-detail'),
    path('libary/author/<int:pk>', views.authorDetails, name='author-detail'),
    path('libary/authors/',views.AuthorList.as_view(), name='author_list'),
    path('libary/borrowed/',views.borrowedbooklist, name='borrowed_list'),
    path('libary/borrowed/user/',views.borrowedbooklistUser, name='borrowed_list_user'),
    path('libary/renew/<uuid:pk>/book',views.renewalform, name='renewalform'),
    path('libary/accounts/register', views.register , name='register'),
    path('libary/search/', views.search , name='search'),
    path('libary/book/add',views.BookAdd.as_view(), name='book_add'),
    path('libary/book/<int:pk>/update',views.BookUpdate.as_view(), name='book_update'),
    path('libary/book/<int:pk>/delete',views.BookDelete.as_view(), name='book_delete'),
    path('libary/author/add',views.AuthorAdd.as_view(), name='author_add'),
    path('libary/author/<int:pk>/update',views.AuthorUpdate.as_view(), name='author_update'),
    path('libary/author/<int:pk>/delete',views.AuthorDelete.as_view(), name='author_delete'),


]
