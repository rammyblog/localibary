import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, BookInstance, Author, Comment, AuthorComment
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.views import generic 
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from .forms import RenewalForm, Register, CommentForm, AuthorCommentForm
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.utils.datastructures import MultiValueDictKeyError



def index(request):
	book_instance = BookInstance.objects.filter(status__exact = 'a')
	new_books = Book.objects.all()[:10]
	book_status = BookInstance.objects.filter(Q(status__exact = 'm' ) | Q(status__exact = 'o' ))[:4]
	author = Author.objects.all()[:4]
	context = {'new_books':new_books, 'book_status':book_status, 'author':author, 'book_instance':book_instance}
	return render(request, 'LocalLibary/index.html', context)



class BookList(generic.ListView):
	model = Book
	context_object_name = 'book_list'
	paginate_by=5


def bookDetails(request, pk):
	book = get_object_or_404(Book, pk=pk)
	comments = book.comments.order_by('-created_at')
	# comments = Comment.objects.all()
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = form.save(commit = False)
			if request.user.is_authenticated:
				new_comment.name = request.user.username
			new_comment.author_id = book.author.id
			new_comment.book_id = book.id
			new_comment.save()

			return redirect('book-detail',pk)

	else:
		form = CommentForm()
	context = {'book':book, 'form': form, 'comments':comments}
	return render(request, 'LocalLibary/book_details.html', context)


def authorDetails(request, pk):
	author = get_object_or_404(Author, pk=pk)
	comments = author.author_comment.order_by('-created_at')
	if request.method == 'POST':
		form = AuthorCommentForm(request.POST)
		if form.is_valid():
			new_comment = form.save(commit = False)
			if request.user.is_authenticated:
				new_comment.name = request.user.username
			new_comment.author_id = author.id
			new_comment.save()

			return redirect('author-detail',pk)

	else:
		form = AuthorCommentForm()
	context = {'author':author, 'form': form, 'comments':comments}
	return render(request, 'LocalLibary/author_details.html', context)

def home(request):
	return redirect('index')

class AuthorList(generic.ListView):
	model = Author
	context_object_name = 'author_list'
	paginate_by =10


@permission_required('LocalLibary.can_mark_returned')
def borrowedbooklist(request):
	borrowed = BookInstance.objects.filter(status__exact = 'o').order_by('due_back')
	context = {'borrowed':borrowed}
	return render(request, 'LocalLibary/borrowed_list.html', context)


@login_required
def borrowedbooklistUser(request):
	borrowed = BookInstance.objects.filter(borrower=request.user).filter(status__exact = 'o').order_by('due_back')
	context = {'borrowed':borrowed}
	return render(request, 'LocalLibary/borrowed_list_user.html', context)


@permission_required('LocalLibary.can_mark_returned')
def renewalform(request, pk):
	book = get_object_or_404(BookInstance, pk=pk)
	if request.method=='POST':
		form = RenewalForm(request.POST)
		if form.is_valid():
			book.due_back = form.cleaned_data['renewal_date']
			book.save()
			return HttpResponseRedirect(reverse('borrowed_list'))
	else:
		proposed_date = datetime.date.today() + datetime.timedelta(weeks = 4)
		form = RenewalForm(initial = {'renewal_date':proposed_date})

	context = {'form':form}

	return render(request, 'LocalLibary/renew.html', context)



def register(request):
	if request.method == 'POST':
		form = Register(request.POST)
		if form.is_valid:
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']

			user = authenticate (username = username, password = password)
			login(request, user)
			return redirect(index)

	else:
		form = Register()
	context = {'form':form}

	return render(request, 'registration/register.html', context)

class BookAdd(LoginRequiredMixin, CreateView):
	model = Book
	fields = '__all__'
	template_name = 'LocalLibary/book_add.html'

class BookUpdate(LoginRequiredMixin, UpdateView):
	model = Book
	fields = '__all__'
	template_name = 'LocalLibary/book_add.html'

class BookDelete(LoginRequiredMixin, DeleteView):
	model = Book
	template_name = 'LocalLibary/book_delete.html'
	success_url = reverse_lazy('index')



class AuthorAdd(LoginRequiredMixin, CreateView):
	model = Author
	fields = '__all__'
	template_name = 'LocalLibary/book_add.html'

class AuthorUpdate(LoginRequiredMixin, UpdateView):
	model = Author
	fields = '__all__'
	template_name = 'LocalLibary/book_add.html'

class AuthorDelete(LoginRequiredMixin, DeleteView):
	model = Author
	template_name = 'LocalLibary/book_delete.html'
	success_url = reverse_lazy('index')


def search(request):
	try:
		if request.method == 'GET':
			author = Author.objects.filter(Q(first_name__icontains = request.GET['q']) | Q(last_name__icontains = request.GET['q']))
			search = Book.objects.filter(Q(title__icontains = request.GET['q']) |Q(isbn__icontains = request.GET['q']))
			if search or author:
				context = {'search':search, 'author':author}
				return render(request, 'LocalLibary/search.html', context)
			else:
				return render(request, 'LocalLibary/404.html')

	except MultiValueDictKeyError as e:
		return render(request, 'LocalLibary/404.html')
