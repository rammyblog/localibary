from django.db import models
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from datetime import date



class Genre(models.Model):
	genre = models.CharField(max_length=100, help_text = 'Enter Genre(s) of the book')

	def __str__(self):
		return self.genre


class Language(models.Model):
	language = models.CharField(max_length=50, help_text='Enter the Language in which the book is written')

	def __str__(self):
		return self.language


class Book(models.Model):
	title = models.CharField(max_length=200, help_text='Enter title of the book')
	summary = models.CharField(max_length=10000, help_text='Enter Summary of the book')
	isbn = models.CharField(max_length=13 , help_text='Enter the 13 digits  ISBN of the book ')
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null= True)
	language = models.ForeignKey('Language', on_delete=models.SET_NULL, null= True)
	genre = models.ManyToManyField('Genre', help_text= "Enter Genre(s)")
	book_image = models.ImageField(null = True, blank = True)
	pub_date = models.DateField(null=True)

	def __str__(self):
		return f'{self.title}, {self.author}'
	def get_absolute_url(self):
		return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
	id = models.UUIDField(primary_key=True, default = uuid.uuid4, help_text = "Unique Text of Book")
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length =200, help_text='Enter imprint of book')
	due_back = models.DateField(null=True, blank=True)
	borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	LOAN_STATUS = (

		('m', 'Mainteanance'),
		('o', 'On Loan'),
		('a', 'Available'),
		('r', 'reserved'),
		
		)

	status = models.CharField(
		max_length=1,
		choices = LOAN_STATUS,
		default = 'm',
		blank = True,
		help_text = 'Availability Of Book'
		)

	class Meta:
		ordering = ['due_back']
		permissions = (("can_mark_returned", "Set book as returned"),("can_edit_status", "Set status of book"))

		# permissions = (("can_mark_returned", "Set book as returned"),)


	@property
	def is_overdue(self):
		if self.due_back and date.today() > self.due_back:
			return True
		return False


	def __str__(self):
		return f'{self.id}, {self.imprint}'


class Author(models.Model):
	first_name = models.CharField(max_length=200, help_text='Enter Frist Name of the Author')
	last_name = models.CharField(max_length=10000, help_text='Enter Last Name Of The Author')
	date_of_birth = models.DateField()
	date_of_death = models.DateField('Died', null=True, blank=True)
	author_image = models.ImageField(null = True, blank = True)
	about = models.CharField(max_length=100000, null=True, blank=True)
	# country = models.CharField(max_length =50, null= True, blank= True)

	class Meta:
		ordering = ['last_name', 'first_name']

	def __str__(self):
		return f'{self.last_name}, {self.first_name}'

	def get_absolute_url(self):
		return reverse ('author-detail', args=[str(self.id)])

class Comment(models.Model):
	name = models.CharField(max_length = 30)
	message = models.TextField(max_length= 4000)
	book = models.ForeignKey(Book, related_name= 'comments' , on_delete=models.CASCADE)
	author = models.ForeignKey(Author, related_name= 'author_comments' , on_delete=models.CASCADE) 
	created_at = models.DateField(auto_now_add = True)

	class Meta:
		ordering = ['created_at']

	def __str__(self):
		return self.message

class AuthorComment(models.Model):
	name = models.CharField(max_length = 30)
	message = models.TextField(max_length= 4000)
	author = models.ForeignKey(Author, related_name= 'author_comment' , on_delete=models.CASCADE) 
	created_at = models.DateField(auto_now_add = True)

	class Meta:
		ordering = ['created_at']
		
	def __str__(self):
		return self.message